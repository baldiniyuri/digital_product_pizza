from django_filters import rest_framework as filters
from address.models import Address


class AddressFilters(filters.FilterSet):
    class Meta:
        model = Address
        fields = ['id','street_address', 'city', 'state', 'postal_code']


