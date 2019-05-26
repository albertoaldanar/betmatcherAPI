"""Users urls"""
from django.urls import path

#Views
from cride.events.views import home_data

urlpatterns = [
  path("home_data/", home_data),
]
