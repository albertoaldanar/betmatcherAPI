"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.matches.models import Match
#Django
from django.db import models

#Serializer
from cride.events.serializers import EventModelSerializer
from cride.users.serializers import UserModelSerializer

class MatchModelSerializer(serializers.ModelSerializer):
  back_user = UserModelSerializer(read_only = True)
  lay_user = UserModelSerializer(read_only = True)
  event = EventModelSerializer(read_only = True)

  class Meta:
    """Meta class"""
    model = Match
    fields= (
      "id", "event", "back_user", "back_team",
      "lay_user", "lay_team", "looser",
      "is_finished", "amount", "winner", "quote"
    )

