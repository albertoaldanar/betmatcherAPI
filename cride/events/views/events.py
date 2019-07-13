"""Events API views"""
#DRF
from rest_framework.views import APIView
from rest_framework import status, mixins, viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import generics
from operator import itemgetter, attrgetter
#Django
from django.db.models import Q
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
from cride.users.models import User


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
      current_user = request.query_params.get("current_user")
      user = User.objects.get(username = current_user)

      sports = Sport.objects.filter(show = True)

      events = Event.objects.filter(
        top_event = True,
        is_finished = False
      ).order_by("date")

      leagues = League.objects.filter(show = True).order_by('order')

      requests = Request.objects.filter(
        ~Q(back_user = user),
        is_public = True,
        is_matched = False,
        event__is_finished= False,
      )

      evs = sorted(events, key=attrgetter("traded"), reverse = True)[:10]

      rqs = sorted(requests, key=attrgetter("created"), reverse = True)[:15]

      data = {
        "top_traded": EventDesignModelSerializer(evs, many= True).data,
        "leagues": LeagueModelSerializer(leagues, many = True).data,
        "top_request": RequestModelSerializer(rqs, many = True).data,
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


# @api_view(["GET"])
# def top_credentials(request):
#       current_user = request.query_params.get("current_user")
#       user = User.objects.get(username = current_user)

#       requests = Request.objects.filter(
#         ~Q(back_user = user),
#         is_public = True,
#         is_matched = False,
#         event__is_finished= False,
#       )

#       events = Event.objects.filter(
#         top_event = True,
#         is_finished = False
#       ).order_by("date")

#       evs = sorted(events, key=attrgetter("traded"), reverse = True)[:10]
#       rqs = sorted(requests, key=attrgetter("created"), reverse = True)[:15]

#       data = {
#         "sports": SportDesignModelSerializer(sports, many = True).data
#       }

#       return Response(data)
