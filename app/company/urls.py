from django.urls import path
from .views import CompanyView


urlpatterns = [
    path('company/', CompanyView.as_view()),
    path('company/<int:company_id>/<int:user_id>/', CompanyView.as_view()),
]
