"""Users urls"""
from django.urls import path

#Views
from cride.users.views import login, signup, verify

urlpatterns = [
  path("users/login", login),
  path("users/signup", signup)
]
