"""Users urls"""
from django.urls import path, include

#Views
from cride.betfriends.views import betfriends_data, create_friendship, decline_request, create_request
from rest_framework.routers import DefaultRouter
# from .views import betfriends as bfrequests_views

# router  = DefaultRouter()
# router.register(r"bfrequest", bfrequests_views.FriendRequestViewSet, basename = "bfrequest")
urlpatterns = [
  path("betfriends_data/", betfriends_data),
  path("create_friendship/", create_friendship),
  path("decline_request/", decline_request),
  path("create_request/", create_request)
  # path("", include(router.urls))
]


