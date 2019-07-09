"""Matches model design"""
#Django
from django.db import models
#Utils
from cride.utils.models import BetmatcherModel

class Match(BetmatcherModel):

  description = models.SlugField(max_length = 225)

  back_user = models.ForeignKey(
    "users.User",
    related_name = "back_user",
    on_delete = models.CASCADE
  )
  back_team = models.CharField(max_length = 20, unique = False)

  winner = models.CharField(max_length = 20, null = True, blank = True)

  looser = models.CharField(max_length = 20, null = True, blank = True)

  draw = models.BooleanField(default = False)
  quote = models.IntegerField(null = True)

  event = models.ForeignKey(
    "events.Event",
    related_name = "event",
    on_delete = models.CASCADE
  )

  request = models.ForeignKey(
    "matches.Request",
    related_name = "request",
    on_delete = models.CASCADE
  )

  lay_user = models.ForeignKey(
    "users.User",
    related_name = "lay_user",
    on_delete = models.CASCADE
  )

  lay_team = models.CharField(max_length = 20, unique = False)

  is_finished = models.BooleanField(default = False)
  amount = models.PositiveIntegerField(default = 0)

  def __str__(self):
    return self.event.name

  class Meta(BetmatcherModel.Meta):
    ordering = ["-created", "-modified"]
