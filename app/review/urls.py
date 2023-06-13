from django.urls import path
from .views import ReviewView


urlpatterns = [
    path('review/', ReviewView.as_view()),
    path('review/<int:review_id>/<int:user_id>/', ReviewView.as_view()),
]
