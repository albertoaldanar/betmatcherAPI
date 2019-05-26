"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.events.models import Sport
#Django
from django.db import models

class SportModelSerializer(serializers.ModelSerializer):

  class Meta:
    """Meta class"""
    model = Sport
    fields= (
      "name", "icon",
    )

