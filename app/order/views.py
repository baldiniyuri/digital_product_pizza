from order.models import Order
from order.serializers import OrderSerializers, OrderGetSerializers
from order.filters import OrdersFilters
from order.utils import OrderUtils
from core.utils import CoreUtils
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


CORE = CoreUtils()


class OrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    filter_set_class = OrdersFilters
    serializer_class = OrderGetSerializers


    def post(self, request):
            serializer = OrderSerializers(data=request.data)
            
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if CORE.check_user_token(request=request, user_id=request.data["user_id"]):
                order = OrderUtils(request)
                response = order.create_order()

                if not response[0]:
                    missing_models = response[1]
                    return Response(
                        {"Detail": "One or more relations not found", "Missing Models": missing_models},
                        status=status.HTTP_404_NOT_FOUND
                    )

                serializer = self.serializer_class(response[1])
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(status=status.HTTP_401_UNAUTHORIZED)



    def get(self, request):
        query = request.query_params.get('query', '')
        param = request.query_params.get('param', '')
        user_id = request.query_params.get('user_id', '')

        if not CORE.find_user(user_id):
            return Response(status=status.HTTP_404_NOT_FOUND)


        if CORE.check_user_token(request=request, user_id=user_id):
            queryset_filters = {
                "id": {"pk": query},
                "customer": {"customer__name__icontains": query},
                "company": {"company__cnpj": query},
                "delivery_address": {"delivery_address__street_address": query},
                "status": {"status": query}
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
    

    def delete(self, request, order_id: int, user_id: int):
        if CORE.check_user_token(request=request, user_id=user_id):
            order = self.queryset.filter(id=order_id, customer_id=user_id)

            if order:
                order.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

