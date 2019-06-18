"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.betfriends.models import BetFriend
from cride.users.models import User
#Django
from django.db import models
#Serializer
from cride.users.serializers import UserModelSerializer

class UserModelSerializer(serializers.ModelSerializer):
  user_a = UserModelSerializer(read_only = True)
  user_b = UserModelSerializer(read_only = True)

  class Meta:
    model = BetFriend
    fields= (
      "user_a", "user_b",
    )

