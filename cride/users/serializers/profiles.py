"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.users.models import User, Profile
from django.db import models

class ProfileModelSerializer(serializers.ModelSerializer):

  class Meta:
    model = Profile
    fields = (
      "lost", "won", "draw", "country",
      "efficiency", "picture", "coins"
    )
