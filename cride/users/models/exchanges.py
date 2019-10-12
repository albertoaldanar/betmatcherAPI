from django.db import models

#Utilities
from cride.utils.models import BetmatcherModel

class Exchange(BetmatcherModel):

  user = models.ForeignKey(
    "users.User",
    on_delete = models.CASCADE,
    related_name = "user"
  )

  prize = models.ForeignKey(
    "users.Prize",
    on_delete = models.CASCADE,
    related_name = "prize"
  )

  date = models.DateTimeField(
    "event_date",
    help_text = "Date of the event"
  )

  def __str__(self):
    return self.user.username

