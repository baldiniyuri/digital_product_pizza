from pizza.models import Pizza
from pizza.serializers import PizzaSerializers
from pizza.filters import PizzaFilters
from core.utils import CoreUtils
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


CORE = CoreUtils()


class PizzaView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Pizza.objects.all()
    filter_set_class = PizzaFilters
    serializer_class = PizzaSerializers


    def get(self, request):
        query = request.query_params.get('query', '')
        param = request.query_params.get('param', '')
        user_id = request.query_params.get('user_id', '')

        if not CORE.find_user(user_id):
            return Response(status=status.HTTP_404_NOT_FOUND)
        

        if CORE.check_user_token(request=request, user_id=user_id):
            queryset_filters = {
                "id": {"pk": query},
                "flavor": {"flavor": query},
                "second_flavor": {"second_flavor": query},
                "is_two_flavors": {"is_two_flavors": query},
            }
            
            found_address = None
       
            for key, lookup in queryset_filters.items():
                if param == key:
                    found_address = self.queryset.filter(**queryset_filters[param])
                    break

            if not found_address:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializers = self.serializer_class(found_address, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    

    def delete(self, request, pizza_id: int, user_id: int):
        if CORE.check_user_token(request=request, user_id=user_id):
            pizza = self.queryset.filter(id=pizza_id, user_id=user_id)

            if pizza:
                pizza.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

