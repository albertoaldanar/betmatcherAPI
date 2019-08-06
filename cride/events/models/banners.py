#Django
from django.db import models

#Utilities
from cride.utils.models import BetmatcherModel

class Banner(BetmatcherModel):

  title = models.TextField(max_length= 400, blank = True)
  message = models.TextField(max_length= 400, blank = True)
  img = models.TextField(max_length = 500, blank = True)
  order = models.PositiveIntegerField(null = True)
  
  def __str__(self):
    return self.title