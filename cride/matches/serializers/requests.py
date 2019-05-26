"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.matches.models import Request
#Django
from django.db import models

#Serializer
from cride.users.serializers import UserModelSerializer
from cride.events.serializers import EventModelSerializer

class RequestModelSerializer(serializers.ModelSerializer):
  back_user = UserModelSerializer(read_only = True)
  event = EventModelSerializer(read_only = True)

  class Meta:
    """Meta class"""
    model = Request
    fields= (
      "back_user", "back_team", "event",
      "is_matched", "amount", "is_public"
    )

