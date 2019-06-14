"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.events.models import League
#Django
from django.db import models

class LeagueModelSerializer(serializers.ModelSerializer):

  class Meta:
    model = League
    fields= (
      "name", "image", "img"
    )

