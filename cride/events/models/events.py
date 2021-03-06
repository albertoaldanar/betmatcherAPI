#Django
from django.db import models

#Utilities
from cride.utils.models import BetmatcherModel

class Event(BetmatcherModel):
  top_event = models.BooleanField(default = False)
  in_play = models.BooleanField(default = False)
  is_finished = models.BooleanField(default = False)
  half_time = models.BooleanField(default = False)
  second_time = models.BooleanField(default = False)

  added_time = models.SmallIntegerField(default = 0)
  name = models.CharField(max_length = 30, unique = False, null = True)
  league = models.ForeignKey(
    "events.League",
    on_delete = models.CASCADE
  )
  sport = models.ForeignKey(
    "events.Sport",
    on_delete = models.CASCADE
  )

  time = models.CharField(null = True, blank = True, max_length = 30)
  minute = models.SmallIntegerField(default = 0)
  
  img = models.TextField(max_length = 500, blank = True, null= True)
  
  score_local = models.PositiveIntegerField(default = 0)
  score_visit = models.PositiveIntegerField(default = 0)

  local_tennis = models.CharField(null = True, blank = True, max_length = 30)
  visit_tennis = models.CharField(null = True, blank = True, max_length = 30)

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
  relation_v_l = models.SmallIntegerField(null = True)

  relation_l_d = models.SmallIntegerField(null = True, blank = True)
  relation_d_l = models.SmallIntegerField(null = True, blank = True)

  relation_v_d = models.SmallIntegerField(null = True, blank = True)
  relation_d_v = models.SmallIntegerField(null = True, blank = True)

  def __str__(self):
    return self.name
