"""User model"""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
#Utilities
from cride.utils.models import BetmatcherModel
from django.core.validators import RegexValidator

class User(BetmatcherModel, AbstractUser):
  """User model"""
    email = models.EmailField(
    "email addres",
    unique = True,
    error_messages = {
      "unique": "Username aleready taken"
    }
  )

  phone_regex = RegexValidator(
    regex = r'\+?1?\d{9,15}$',
    message = "Phone number must be entered"
  )

  phone_number = models.CharField( validators = [phone_regex], max_length = 17, blank = True)

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["username", "first_name", "last_name"]

  is_client = models.BooleanField(
    "client_status",
    default = True,
    help_text = (
      "Help easylit",
      "Clients are the main users"
    )
  )

  is_verified = models.BooleanField(
    "verified",
    default = True,
    help_text = "True if the user is verified"
  )

  def __str__(self):
    return self.username

  def get_short_name(self):
    return self.username
