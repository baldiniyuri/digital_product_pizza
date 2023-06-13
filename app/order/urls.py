from django.urls import path
from .views import OrderView


urlpatterns = [
    path('order/', OrderView.as_view()),
    path('order/<int:order_id>/<int:user_id>/', OrderView.as_view()),
]
