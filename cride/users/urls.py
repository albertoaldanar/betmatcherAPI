# """Users urls"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# #Views
# from cride.users.views import login, signup, verify

# urlpatterns = [
#   path("users/login", login),
#   path("users/signup", signup)
# ]
#DRF
from .views import users as user_views

router = DefaultRouter()
router.register(r"users", user_views.UserViewSet, basename = "users")

urlpatterns= [
  path("", include(router.urls))
]
