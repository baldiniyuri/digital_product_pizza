from django.urls import path
from .views import AddressView


urlpatterns = [
    path('address/', AddressView.as_view()),
    path('address/<int:address_id>/<int:user_id>/', AddressView.as_view()),
]
