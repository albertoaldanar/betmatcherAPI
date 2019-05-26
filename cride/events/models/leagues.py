#Django
from django.db import models

#Utils
from cride.utils.models import BetmatcherModel

class League(BetmatcherModel):
  """League model"""
  name = models.CharField(max_length = 15, blank = False)
  sport = models.ForeignKey(
    "events.Sport",
    on_delete = models.CASCADE
  )
  show = models.BooleanField(default = True)
  order = models.PositiveIntegerField(null = True)

  image = models.ImageField(
    "league_image",
    upload_to = "users/pictures",
    blank = False,
  )

  def __str__(self):
    return self.name
