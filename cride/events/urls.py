"""Users urls"""
from django.urls import path, include
#Views
from cride.events.views import home_data, top_events, user_activity
from .views import leagues as leagues_views
from .views import events as events_views
#DRF
from rest_framework.routers import DefaultRouter

router  = DefaultRouter()
router.register(r"leagues", leagues_views.LeaguesViewSet, basename = "leagues")
router.register(r"events", events_views.EventsViewSet, basename = "events")

urlpatterns = [
  path("home_data/", home_data),
  path("top_events/", top_events),
  path("user_activity/", user_activity),
  path("", include(router.urls))
]