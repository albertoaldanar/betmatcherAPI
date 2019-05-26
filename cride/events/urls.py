"""Users urls"""
from django.urls import path

#Views
from cride.events.views import home_data, top_events

urlpatterns = [
  path("home_data/", home_data),
  path("top_events/", top_events),
]
