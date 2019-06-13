from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import action

#Serializers
from cride.events.serializers import LeagueModelSerializer
#models
from cride.events.models import Event, League

class LeaguesViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
  """Event view set"""

  serializer_class = LeagueModelSerializer

  def get_queryset(self):
        sport = self.request.query_params.get("sport")

        queryset = League.objects.filter(
          sport__name = sport,
        )
        return queryset
