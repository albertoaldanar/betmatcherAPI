"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.betfriends.models import FriendRequest
from cride.users.models import User
#Django
from django.db import models
#Serializer
from cride.users.serializers import UserModelSerializer

class FriendRequestModelSerializer(serializers.ModelSerializer):
  sent_by = UserModelSerializer(read_only = True)
  received_by = UserModelSerializer(read_only = True)

  class Meta:
    model = FriendRequest
    fields= (
      "sent_by", "received_by", "is_accepted"
    )

