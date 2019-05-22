#Django
from django.db import models

#Utilities
from cride.utils.models import BetmatcherModel

class Sport(BetmatcherModel):
  name = models.CharField(max_length = 15, unique= True)
  icon = models.ImageField(
    "sport_icon",
    upload_to = "users/pictures",
    blank = False,
  )
  show = models.BooleanField(default = True)

  def __str__(self):
    return self.name

  class Meta(BetmatcherModel.Meta):
    ordering = ["-created", "-modified"]
