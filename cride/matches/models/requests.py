"""Request models design """

#Django
from django.db import models

#Utilis
from cride.utils.models import BetmatcherModel

class Request(BetmatcherModel):
  back_user = models.ForeignKey(
    "users.User",
    on_delete = models.CASCADE
  )
  event = models.ForeignKey(
    "events.Event",
    on_delete = models.CASCADE
  )

  back_team = models.CharField(max_length = 20, unique = False)
  opponent = models.CharField(max_length = 20, unique = False)
  message = models.TextField(max_length= 300, blank = True, null = True)

  fq = models.IntegerField(null = True)
  sq = models.IntegerField(blank=True, null=True)
  fq_position = models.IntegerField(null = True)
  sq_position = models.IntegerField(blank=True, null=True)

  is_matched = models.BooleanField(default = False)
  amount = models.PositiveIntegerField(default = 0)
  is_public = models.BooleanField(default = True)
  declined = models.BooleanField(default = False)

  def __str__(self):
    return self.back_user.username

  class Meta(BetmatcherModel.Meta):
    ordering = ["-created", "-modified"]
