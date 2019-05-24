#Django
from django.db import models

#Utilities
from cride.utils.models import BetmatcherModel

class Event(BetmatcherModel):
  top_event = models.BooleanField(default = False)
  in_play = models.BooleanField(default = False)
  league = models.ForeignKey(
    "events.League",
    on_delete = models.CASCADE
  )
  sport = models.ForeignKey(
    "events.Sport",
    on_delete = models.CASCADE
  )
  score_local = models.PositiveIntegerField(default = 0)
  score_visit = models.PositiveIntegerField(default = 0)

  local = models.ForeignKey(
    "events.Team",
    on_delete = models.CASCADE,
    related_name = "local_team"
  )
  visit = models.ForeignKey(
    "events.Team",
    on_delete = models.CASCADE,
    related_name = "visit_team"
  )

  date = models.DateTimeField(
    "event_date",
    help_text = "Date of the event"
  )
  traded = models.PositiveIntegerField(null = True)
  top_bet = models.PositiveIntegerField(null = True)
  matched_bets = models.PositiveIntegerField(null = True)
  unmatched_bets = models.PositiveIntegerField(null = True)

  position_local = models.PositiveSmallIntegerField(default = 0)
  position_visit = models.PositiveSmallIntegerField(default = 0)
  position_draw = models.PositiveSmallIntegerField(default = 0)
  relation_l_v = models.SmallIntegerField(null = True)
  relation_l_d = models.SmallIntegerField(null = True)
  relation_v_d = models.SmallIntegerField(null = True)

