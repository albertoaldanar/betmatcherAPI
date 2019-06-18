#Django
from django.db import models
#Utilities
from cride.utils.models import BetmatcherModel

class FriendRequest(BetmatcherModel):
  sent_by = models.ForeignKey(
    "users.User",
    related_name = "sent_by",
    on_delete = models.CASCADE
  )
  received_by = models.ForeignKey(
    "users.User",
    related_name = "received_by",
    on_delete = models.CASCADE
  )
  is_accepted = models.BooleanField(default = False)

