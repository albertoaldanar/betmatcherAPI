"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.users.models import Exchange
from django.db import models

from cride.users.serializers import (
  UserModelSerializer,
  PrizeModelSerializer,
)

class ExchangeModelSerializer(serializers.ModelSerializer):

  user = UserModelSerializer(read_only= True)
  prize = PrizeModelSerializer(read_only= True)

  class Meta:
   	model = Exchange
   	fields = (
      "user", "prize", "date",
    )
