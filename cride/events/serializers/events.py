# """Users Seliralizers"""
# #DRF
# from rest_framework import serializers
# #Models
# from cride.events.models import Event
# #Django
# from django.db import models

# #Serializer
# from cride.events.serializers import TeamModelSerializer

# class EventModelSerializer(serializers.ModelSerializer):
#   back_user = UserModelSerializer(read_only = True)

#   class Meta:
#     """Meta class"""
#     model = Request
#     fields= (
#       "back_user", "back_team", "event",
#       "is_matched", "amount", "is_public"
#     )


