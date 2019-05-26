"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.events.models import Event
#Django
from django.db import models

#Serializer
from cride.events.serializers import TeamModelSerializer

class EventModelSerializer(serializers.ModelSerializer):

  local = TeamModelSerializer(read_only = True)
  visit = TeamModelSerializer(read_only = True)

  class Meta:
    """Meta class"""
    model = Event
    fields= (
      "traded", "matched_bets", "local", "unmatched_bets", "visit"
    )


