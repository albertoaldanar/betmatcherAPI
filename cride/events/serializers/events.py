"""Users Seliralizers"""
#DRF
from rest_framework import serializers
#Models
from cride.events.models import Event
#Django
from django.db import models

#Serializer
from cride.events.serializers import (
  TeamModelSerializer,
  LeagueModelSerializer,
  SportModelSerializer
)

class EventDesignModelSerializer(serializers.BaseSerializer):

  def to_representation(self, obj):

        if obj.sport.name == "Soccer":
          return {
              'local': {
                'name': obj.local.name,
                'quotes': {obj.position_visit: obj.relation_l_v, obj.position_draw: obj.relation_l_d,},
                'position': obj.position_local
              },
              'draw': {
                'name': "Draw",
                'quotes': {obj.position_local: obj.relation_l_d, obj.position_visit: obj.relation_v_d},
                'position': obj.position_draw
              },
              'visit': {
                'name': obj.visit.name,
                'quotes': {obj.position_local: obj.relation_l_v, obj.position_draw: obj.relation_v_d},
                'position': obj.position_visit
              },
              "data": EventModelSerializer(obj).data
          }
        else:
          return {
              'local': {
                'name': obj.local.name,
                'quotes': obj.relation_l_v,
                'position': obj.position_local
              },
              'visit': {
                'name': obj.visit.name,
                'quotes': obj.relation_l_v,
                'position': obj.position_visit
              },
              "data": EventModelSerializer(obj).data
          }

class EventModelSerializer(serializers.ModelSerializer):

  sport = SportModelSerializer(read_only = True)
  league = LeagueModelSerializer(read_only = True)
  local = TeamModelSerializer(read_only = True)
  visit = TeamModelSerializer(read_only = True)

  class Meta:
    """Meta class"""
    model = Event
    fields= (
      "name", "date", "traded", "unmatched_bets",
      "matched_bets", "score_local", "score_visit",
      "sport", "league", "top_bet", "name", "in_play",
      "local", "visit"
    )


