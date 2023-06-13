from django.urls import path
from .views import  LoginView, LogoutView, UserView


urlpatterns = [
    path('register/', UserView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/<int:user_id>/', LogoutView.as_view()),
]
