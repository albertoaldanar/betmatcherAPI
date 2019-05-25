"""Matches model design"""
#Django
from django.db import models
#Utils
from cride.utils.models import BetmatcherModel

class Match(BetmatcherModel):
  back_user = models.ForeignKey(
    "users.User",
    related_name = "user_lay",
    on_delete = models.CASCADE
  )
  back_team = models.CharField(max_length = 20, unique = False)

  request = models.ForeignKey(
    "matches.Request",
    related_name = "request",
    on_delete = models.CASCADE
  )

  lay_user = models.ForeignKey(
    "users.User",
    related_name = "back_user",
    on_delete = models.CASCADE
  )

  lay_team = models.CharField(max_length = 20, unique = False)

  is_finished = models.BooleanField(default = False)
  amount = models.PositiveIntegerField(default = 0)

  def __str__(self):
    return self

  class Meta(BetmatcherModel.Meta):
    ordering = ["-created", "-modified"]
