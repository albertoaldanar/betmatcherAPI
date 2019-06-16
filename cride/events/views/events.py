"""Events API views"""
#DRF
from rest_framework.views import APIView
from rest_framework import status, mixins, viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import generics
#Serializer
from cride.events.serializers import(
  LeagueModelSerializer,
  EventModelSerializer,
  EventDesignModelSerializer,
  SportDesignModelSerializer
)
from cride.matches.serializers import RequestModelSerializer
#Utilities
from heapq import nlargest
#Models
from cride.events.models import League, Event, Sport
from cride.matches.models import Request


class EventsViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
  """Event view set"""

  serializer_class = EventDesignModelSerializer

  def get_queryset(self):
        league = self.request.query_params.get("league")

        queryset = Event.objects.filter(
          league__name = league,
        )
        return queryset


@api_view(["GET"])
def home_data(request):
      sports = Sport.objects.filter(show = True)

      events = Event.objects.filter(
        top_event = True,
        is_finished = False
      ).order_by("date")

      leagues = League.objects.filter(show = True).order_by('order')

      requests = Request.objects.filter(
        is_public = True,
        is_matched = False
      )

      # rqs = sorted(requests, key= requests.amount, reverse=True)[:5]

      data = {
        "top_traded": EventDesignModelSerializer(events, many= True).data,
        "leagues": LeagueModelSerializer(leagues, many = True).data,
        "top_request": RequestModelSerializer(requests, many = True).data,
        "sports": SportDesignModelSerializer(sports, many = True).data
      }
      return Response(data)


@api_view(["GET"])
def top_events(request):
      sports = Sport.objects.filter(show = True)

      top_events = Event.objects.filter(
        top_event = True,
        is_finished = False
      ).order_by("date")

      data = {
        "top_events": EventDesignModelSerializer(top_events, many= True).data,
        "sports": SportDesignModelSerializer(sports, many = True).data
      }

      return Response(data)
