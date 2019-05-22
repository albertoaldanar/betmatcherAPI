from django.db import models

#Utilities
from cride.utils.models import BetmatcherModel

class Profile(BetmatcherModel):

  user = models.OneToOneField("users.User", on_delete = models.CASCADE)
  picture = models.ImageField(
    "profile_picture",
    upload_to = "users/pictures",
    blank = True,
    null = True
  )
  country = models.TextField(max_length= 500, blank = True)

  #Stats
  lost = models.PositiveIntegerField(default = 0)
  won = models.PositiveIntegerField(default = 0)
  draw = models.PositiveIntegerField(default = 0)
  efficiency = models.FloatField(
    default = 0,
    help_text = "Reputation for rides offered or taken"
  )
