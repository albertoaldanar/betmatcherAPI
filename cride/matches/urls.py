"""Users urls"""
from django.urls import path, include

#Views
from cride.matches.views import matches
from .views import requests as requests_views
from cride.matches.views import get_requests
#DRF
from rest_framework.routers import DefaultRouter

# router  = DefaultRouter()
# router.register(r"matches", matches_views.MatchesViewSet, basename = "matches")

# urlpatterns = [
#     path("", include(router.urls))
# ]
router  = DefaultRouter()
router.register(r"requests", requests_views.RequestViewSet, basename = "request")

urlpatterns = [
  path("matches/", matches),
  path("get_requests/", get_requests),
  path("", include(router.urls))

]



