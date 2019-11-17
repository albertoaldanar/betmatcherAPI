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
  username = models.CharField(max_length = 20, blank = True, null = True)

  notification_token = models.CharField(
    "notification_token",
    blank = True, null = True,
    max_length = 50,
  )

  #Stats
  lost = models.PositiveIntegerField(default = 0)
  won = models.PositiveIntegerField(default = 0)
  coins = models.PositiveIntegerField(default= 0)
  draw = models.PositiveIntegerField(default = 0)
  efficiency = models.FloatField(
    default = 0,
    help_text = "Reputation for rides offered or taken"
  )

  def __str__(self):
    return self.username

