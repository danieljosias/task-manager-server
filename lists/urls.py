from django.urls import path
from .views import ListView, ListViewDetail


urlpatterns = [
    path("lists/", ListView.as_view()),
    path("lists/<list_id>/", ListViewDetail.as_view()),
]
