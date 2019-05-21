#Django
from django.db import models

#Utilities
from cride.utils.models import BetmatcherModel

class Event(BetmatcherModel):
  name = models.CharField(max_length = 15, unique= True)
  top_event = models.BooleanField(default = False)
  league = models.ForeignKey(
    "events.League",
    on_delete = models.SET_NULL
  )
  sport = models.ForeignKey(
    "events.Sport",
    on_delete = models.SET_NULL
  )
  local = models.CharField(max_length = 15, unique= True)
  visit = models.CharField(max_length = 15, unique= True)

