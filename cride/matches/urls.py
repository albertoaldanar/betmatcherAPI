"""Users urls"""
from django.urls import path, include

#Views
from cride.matches.views import matches
# from .views import matches as matches_views
# from rest_framework.routers import DefaultRouter

# router  = DefaultRouter()
# router.register(r"matches", matches_views.MatchesViewSet, basename = "matches")

# urlpatterns = [
#     path("", include(router.urls))
# ]
urlpatterns = [
  path("matches/", matches)
]
