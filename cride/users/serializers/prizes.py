"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.users.models import Prize
from django.db import models

class PrizeModelSerializer(serializers.ModelSerializer):

  class Meta:
    model = Prize
    fields = (
      "name", "description", "img", "price",
    )
