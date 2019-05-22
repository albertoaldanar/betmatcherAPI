"""Teams for event class"""
#Django
from django.db import models

#Utils
from cride.utils.models import BetmatcherModel

class Team(BetmatcherModel):
  name = models.CharField(max_length = 18, unique= True)
  league = models.ForeignKey(
    "events.League",
    on_delete = models.CASCADE
  )
