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

  adress = models.CharField(max_length = 60, blank = True, null = True)
  phone = models.CharField(max_length = 25, blank = True, null = True)
  email = models.CharField(max_length = 25, blank = True, null = True)
  cp = models.CharField(max_length = 25, blank = True, null = True)
  country = models.CharField(max_length = 25, blank = True, null = True)
  city = models.CharField(max_length = 25, blank = True, null = True)
  full_name = models.CharField(max_length = 55, blank = True, null = True)
  state = models.CharField(max_length = 25, blank = True, null = True)

  date = models.DateTimeField(
    "event_date",
    help_text = "Date of the event"
  )

  def __str__(self):
    return self.user.username

