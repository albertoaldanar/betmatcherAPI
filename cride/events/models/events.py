#Django
from django.db import models

#Utilities
from cride.utils.models import BetmatcherModel

class Event(BetmatcherModel):
  top_event = models.BooleanField(default = False)
  in_play = models.BooleanField(default = False)
  is_finished = models.BooleanField(default = False)
  name = models.CharField(max_length = 30, unique = False, null = True)
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
  traded = models.PositiveIntegerField(default = 0)
  top_bet = models.PositiveIntegerField(default = 0)
  matched_bets = models.PositiveIntegerField(default = 0)
  unmatched_bets = models.PositiveIntegerField(default = 0)

  position_local = models.PositiveSmallIntegerField(default = 0)
  position_visit = models.PositiveSmallIntegerField(default = 0)
  position_draw = models.PositiveSmallIntegerField(null = True, blank = True)
  relation_l_v = models.SmallIntegerField(null = True)
  relation_l_d = models.SmallIntegerField(null = True, blank = True)
  relation_v_d = models.SmallIntegerField(null = True, blank = True)

  def __str__(self):
    return self.name
