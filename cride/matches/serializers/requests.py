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

  back_user = UserModelSerializer()
  event = EventModelSerializer()

  class Meta:
    """Meta class"""
    model = Request
    fields= (
      "id", "back_user", "back_team", "event",
      "is_matched", "amount", "is_public"
    )


class CreateRequestSerializer(serializers.Serializer):
  back_user = UserModelSerializer()
  event = EventModelSerializer()
  back_team = serializers.CharField(max_length =140)
  amount = serializers.IntegerField(default = 0)

  def create(self, data):
    return Request.objects.create(**data)



