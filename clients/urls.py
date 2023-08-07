from django.urls import path
from .views import ClientView


urlpatterns = [
    path('clients/', ClientView.as_view()),
]