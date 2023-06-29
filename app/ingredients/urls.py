from django.urls import path
from .views import IngredientsView


urlpatterns = [
    path('ingredients/', IngredientsView.as_view()),
    path('ingredients/<int:ingredient_id>/<int:user_id>/', IngredientsView.as_view()),
]
