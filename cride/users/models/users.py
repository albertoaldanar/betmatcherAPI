"""User model"""
#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
#Utilities
from cride.utils.models import BetmatcherModel

class User(BetmatcherModel, AbstractUser):
  """User model"""
  email = models.EmailField(
    "email addres",
    unique = True,
    error_messages = {
      "unique": "Username aleready taken"
    }
  )

  country = models.CharField(
    "country",
    max_length = 15,
    help_text = ("User´s country")
  )

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["username", "first_name", "last_name"]


  def __str__(self):
    return self.username

  def get_short_name(self):
    return self.username
