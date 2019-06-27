#django
from django.db import models
from django.contrib import admin
#model
from cride.betfriends.models import BetFriend, FriendRequest

@admin.register(BetFriend)
class BetFriendAdmin(admin.ModelAdmin):
  list_display= (
    "user_a",
    "user_b"
  )

@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
  list_display= (
    "is_accepted",
    "received_by",
    "sent_by",
    "id"
  )
  search_fields = ("sent_by",)


