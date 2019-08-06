"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.events.models import Banner
#Django
from django.db import models

class BannerModelSerializer(serializers.ModelSerializer):

  class Meta:
    model = Banner
    fields= (
      "img", "title", "message", "order"
    )

