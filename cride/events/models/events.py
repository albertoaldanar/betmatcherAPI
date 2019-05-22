#Django
from django.db import models

#Utilities
from cride.utils.models import BetmatcherModel

class Event(BetmatcherModel):
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
  date = models.DateTimeField(
    "event_date",
    help_text = "Date of the event"
  )
  traded = models.PositiveIntegerField(default = 0)
  top_bet = models.PositiveIntegerField(default = 0)
  matched_bets = models.PositiveIntegerField(default = 0)
  unmatched_bets = models.PositiveIntegerField(default = 0)

  position_local = models.PositiveSmallIntegerField(default = 0)
  position_visit = models.PositiveSmallIntegerField(default = 0)
  position_draw = models.PositiveSmallIntegerField(default = 0)
  relation_l_v = models.SmallIntegerField(null = True)
  relation_l_d = models.SmallIntegerField(null = True)
  relation_v_d = models.SmallIntegerField(null = True)

