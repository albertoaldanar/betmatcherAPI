#Django
from django.db import models
#Utilities
from cride.utils.models import BetmatcherModel

class BetFriend(BetmatcherModel):
  user_a = models.ForeignKey(
    "users.User",
    related_name = "user_a",
    on_delete = models.CASCADE
  )
  user_b = models.ForeignKey(
    "users.User",
    related_name = "user_b",
    on_delete = models.CASCADE
  )

  friend_request = models.ForeignKey(
    "betfriends.FriendRequest",
    related_name = "friend_request",
    on_delete = models.CASCADE,
    null=True
  )

