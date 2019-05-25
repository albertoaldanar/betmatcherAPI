"""Request models design """

#Django
from django.db import models

#Utilis
from cride.utils.models import BetmatcherModel

class Request(BetmatcherModel):
  back_user = models.ForeignKey(
    "users.User",
    on_delete = models.CASCADE
  )
  event = models.ForeignKey(
    "events.Event",
    on_delete = models.CASCADE
  )
  back_team = models.CharField(max_length = 20, unique = False)

  is_matched = models.BooleanField(default = False)
  amount = models.PositiveIntegerField(default = 0)
  is_public = models.BooleanField(default = True)

  def __str__(self):
    return self.back_team

  class Meta(BetmatcherModel.Meta):
    ordering = ["-created", "-modified"]
