from django_filters import rest_framework as filters
from order.models import Order


class OrdersFilters(filters.FilterSet):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'company', 'pizzas', 'delivery_address', 'status']


