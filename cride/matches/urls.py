"""Users urls"""
from django.urls import path, include

#Views
from cride.matches.views import matches, post_match
from .views import requests as requests_views
from cride.matches.views import post_request, cancel_request, direct_bets, decline_bet
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
  path("post_request/", post_request),
  path("cancel_request/", cancel_request),
  path("post_match/", post_match),
  path("direct_bets/", direct_bets),
  path("decline_bet/", decline_bet),
  path("", include(router.urls))

]



