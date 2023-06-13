from django_filters import rest_framework as filters
from pizza.models import Pizza


class PizzaFilters(filters.FilterSet):
    class Meta:
        model = Pizza
        fields = ['id','flavor', 'second_flavor', 'is_two_flavors']


