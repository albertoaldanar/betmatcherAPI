"""Users urls"""
from django.urls import path, include
#Views
from cride.events.views import home_data, top_events
from .views import leagues as leagues_views
#DRF
from rest_framework.routers import DefaultRouter

router  = DefaultRouter()
router.register(r"leagues", leagues_views.LeaguesViewSet, basename = "leagues")

urlpatterns = [
  path("home_data/", home_data),
  path("top_events/", top_events),
  path("", include(router.urls))
]
