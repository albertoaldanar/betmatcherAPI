"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.events.models import Team
#Django
from django.db import models

class TeamModelSerializer(serializers.ModelSerializer):

  class Meta:
    """Meta class"""
    model = Team
    fields= (
      "name", "league", "short_name"
    )

