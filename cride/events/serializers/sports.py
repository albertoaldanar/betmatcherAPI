"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.events.models import Sport, League
#Django
from django.db import models

from cride.events.models import Sport

class SportDesignModelSerializer(serializers.BaseSerializer):

  def to_representation(self, obj):

        leagues = League.objects.filter(sport__id = obj.id)
        return {
          "name": obj.name,
          "count": len(leagues)
        }

class SportModelSerializer(serializers.ModelSerializer):

  class Meta:
    """Meta class"""
    model = Sport
    fields= (
      "name", "icon",
    )


