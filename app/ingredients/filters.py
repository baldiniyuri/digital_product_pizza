from django_filters import rest_framework as filters
from ingredients.models import Ingredients


class IngredientsFilters(filters.FilterSet):
    class Meta:
        model = Ingredients
        fields = ['id','ingredient_name']


