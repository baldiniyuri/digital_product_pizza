from review.models import Review
from review.serializers import ReviewSerializers
from review.filters import ReviewFilters
from core.utils import CoreUtils
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


CORE = CoreUtils()


class CompanyView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    filter_set_class = ReviewSerializers
    serializer_class = ReviewFilters


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
                "rating": {"rating": query},
                "company": {"company__cnpj": query},
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
    

    def delete(self, request, review_id: int, user_id: int):
        if CORE.check_user_token(request=request, user_id=user_id):
            review = self.queryset.filter(id=review_id, user_id=user_id)

            if review:
                review.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

