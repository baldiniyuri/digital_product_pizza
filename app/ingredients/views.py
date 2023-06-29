from ingredients.models import Ingredients
from ingredients.serializers import IngredientsSerializers
from ingredients.filters import IngredientsFilters
from pizza.models import Pizza
from pizza.serializers import PizzaSerializers, PizzaIngredients
from core.utils import CoreUtils
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


CORE = CoreUtils()


class IngredientsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Ingredients.objects.all()
    filter_set_class = IngredientsFilters
    serializer_class = IngredientsSerializers


    def post(self, request):
        serializers = self.serializer_class(data=request.data)

        if not serializers.is_valid():
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if CORE.check_user_token(request=request, user_id=request.data["user_id"]):
            ingredient_list = []

            ingredients = request.data.pop("ingredient")

            for ingredient in ingredients:
                new_ingredient = self.queryset.get_or_create(ingredient_name=ingredient)[0]
                ingredient_list.append({"id":new_ingredient.id, "ingredient": new_ingredient.ingredient_name})
        
            return Response(ingredient_list, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    

    def put(self, request):
        serializers = PizzaIngredients(data=request.data)

        if not serializers.is_valid():
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if CORE.check_user_token(request=request, user_id=request.data["user_id"]):

            found_pizza = Pizza.objects.filter(id=request.data["pizza_id"])

            if not found_pizza:
                return Response({"detail":"Pizza no found."}, status=status.HTTP_404_NOT_FOUND)

            pizza = Pizza.objects.get(id=request.data["pizza_id"])
            ingredients = request.data.pop("ingredient")

            for ingredient in ingredients:
                new_ingredient = self.queryset.get_or_create(ingredient_name=ingredient["ingredient_name"])[0]
                pizza.ingredients.add(new_ingredient)
                pizza.save()

            serializer = PizzaSerializers(pizza)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


    def get(self, request):
        query = request.query_params.get('query', '')
        param = request.query_params.get('param', '')
        user_id = request.query_params.get('user_id', '')

        if not CORE.find_user(user_id):
            return Response(status=status.HTTP_404_NOT_FOUND)
        

        if CORE.check_user_token(request=request, user_id=user_id):
            queryset_filters = {"id": {"pk": query},"ingredient": {"ingredient": query}}
            
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
    

    def delete(self, request, ingredient_id: int, user_id: int):
        if CORE.check_user_token(request=request, user_id=user_id) and CORE.check_superuser(user_id=user_id):
            ingredient = self.queryset.filter(id=ingredient_id)

            if ingredient:
                ingredient.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

