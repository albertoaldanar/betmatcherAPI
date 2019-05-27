"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.matches.models import Match
#Django
from django.db import models

#Serializer
from cride.events.serializers import EventModelSerializer

class MatchModelSerializer(serializers.ModelSerializer):
  # back_user = UserModelSerializer(read_only = True)
  # event = EventModelSerializer(read_only = True)

  class Meta:
    """Meta class"""
    model = Match
    fields= (
      "back_user", "back_team",
      "lay_user", "lay_team",
      "is_finished", "amount"
    )

