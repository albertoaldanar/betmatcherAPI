"""Django models Utilities"""
from django.db import models

class BetmatcherModel(models.Model):
  """Betmatcher base model"""
  created = models.DateTimeField(
    "created_at",
    auto_now_add = True,
    help_text = "Date tieme when the instance was created"
  )

  modified = models.DateTimeField(
    "modified_at",
    auto_now_add = True,
    help_text = "Date time when object was modified"
  )


  class Meta:
    abstract = True
    get_latest_by = "created"
    ordering = ["-created", "-modified"]
