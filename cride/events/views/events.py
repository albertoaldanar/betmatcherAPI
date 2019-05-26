"""Events API views"""
#DRF
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
#Serializer
from cride.events.serializers import LeagueModelSerializer
from cride.matches.serializers import RequestModelSerializer
#Models
from cride.events.models import League
from cride.matches.models import Request


@api_view(["GET"])
def home_data(request):
      leagues = League.objects.filter(show = True).order_by('order')

      requests = Request.objects.filter(
        is_public = True,
        is_matched = False
      )

      data = {
        "leagues": LeagueModelSerializer(leagues, many = True).data,
        "top_request": RequestModelSerializer(requests, many = True).data,
      }
      return Response(data)
