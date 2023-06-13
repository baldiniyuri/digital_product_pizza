from django.urls import path
from .views import PizzaView


urlpatterns = [
    path('pizza/', PizzaView.as_view()),
    path('pizza/<int:pizza_id>/<int:user_id>/', PizzaView.as_view()),
]
