from django_filters import rest_framework as filters
from company.models import Company


class CompanyFilters(filters.FilterSet):
    class Meta:
        model = Company
        fields = ['id','name', 'cnpj', 'address', 'contact_number', 'email', 'description', 'pizzas']


