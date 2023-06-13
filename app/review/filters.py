from django_filters import rest_framework as filters
from review.models import Review


class ReviewFilters(filters.FilterSet):
    class Meta:
        model = Review
        fields = ['id','customer', 'rating', 'company' ]
