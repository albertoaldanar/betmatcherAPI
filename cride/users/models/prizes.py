from django.db import models
from django.utils.timezone import now

#Utilities
from cride.utils.models import BetmatcherModel

class Prize(BetmatcherModel):

  description = models.TextField(max_length= 500, blank = True)

  name = models.CharField(max_length = 25, blank = True, null = True)
  
  price = models.PositiveIntegerField(default = 0)

  img = models.TextField(max_length = 500, blank = True)

  date = models.DateTimeField(
    "date",
    help_text = "Date of the event",
    default= now
  )

  def __str__(self):
    return self.name

