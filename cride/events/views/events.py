"""Events API views"""
#DRF
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
#Serializer
from cride.events.serializers import LeagueModelSerializer, EventModelSerializer
from cride.matches.serializers import RequestModelSerializer
#Models
from cride.events.models import League, Event
from cride.matches.models import Request


@api_view(["GET"])
def home_data(request):

      events = Event.objects.filter(
        top_event = True
      ).order_by("date")

      leagues = League.objects.filter(show = True).order_by('order')

      requests = Request.objects.filter(
        is_public = True,
        is_matched = False
      )

      serializer_context = {
        'request': Request(request),
      }

      data = {
        "top_traded": EventModelSerializer(events, many= True).data,
        "leagues": LeagueModelSerializer(leagues, many = True).data,
        "top_request": RequestModelSerializer(requests, many = True).data,
      }
      return Response(data)


@api_view(["GET"])
def top_events(request):

      top_events = Event.objects.filter(
        top_event = True
      ).order_by("date")

      data = {
        "top_events": EventModelSerializer(top_events, many= True).data
      }

      return Response(data)
