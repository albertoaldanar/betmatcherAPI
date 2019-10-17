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
from cride.users.views import user_info, user_records, get_all_prizes, pay_prize
from .views import users as user_views

router = DefaultRouter()
router.register(r"users", user_views.UserViewSet, basename = "users")

urlpatterns= [
  path("", include(router.urls)),
  path("user_info/", user_info),
  path("user_records/", user_records),
  path("get_all_prizes/", get_all_prizes),
  path("pay_prize/", pay_prize),
]
