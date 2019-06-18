"""Users urls"""
from django.urls import path, include

#Views
from cride.betfriends.views import betfriends_data, create_friendship
# from rest_framework.routers import DefaultRouter

# router  = DefaultRouter()
# router.register(r"requests", requests_views.RequestViewSet, basename = "request")

urlpatterns = [
  path("betfriends_data/", betfriends_data),
  path("create_friendship/", create_friendship),
]


