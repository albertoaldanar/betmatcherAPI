"""Events API views"""
#DRF
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from itertools import chain
#Django
from django.db.models import Q
#Serializer
from cride.matches.serializers import RequestModelSerializer, MatchModelSerializer
from cride.users.serializers import UserModelSerializer
#Models
from cride.matches.models import Request, Match
from cride.users.models import User
from cride.events.models import Event


@api_view(["GET"])
def matches(request):

      permission_classes = (IsAuthenticated,)

      unmatched_bets = Request.objects.filter(
        is_matched = False,
        back_user = request.user
      ).order_by("created")

      matches = Match.objects.filter(Q(back_user = request.user) | Q(lay_user = request.user)).order_by("event__date")

      matched_bets = matches.filter(event__is_finished = False)
      finished_bets = matches.filter(event__is_finished = True)

      data = {
        "unmatched_bets": RequestModelSerializer(unmatched_bets, many= True).data,
        "matched_bets": MatchModelSerializer(matched_bets, many= True).data,
        "finished_bets": MatchModelSerializer(finished_bets, many= True).data,
      }

      return Response(data)


@api_view(["POST"])
def post_match(request):
      back_user = User.objects.get(username = request.data["back_user"])
      lay_user = User.objects.get(username = request.data["lay_user"])
      event = Event.objects.get(name = request.data["event"])
      req = Request.objects.get(id = request.data["request"])

      quote = request.data["quote"]

      response = Match.objects.create(
        back_user = back_user,
        lay_user = lay_user,
        amount = request.data["amount"],
        back_team = request.data["back_team"],
        lay_team = request.data["lay_team"],
        event = event,
        request = req
      )

      data = {"match": MatchModelSerializer(response).data}

      req.is_matched = True
      req.save()

      l_u = lay_user.profile
      l_u.coins -= quote
      l_u.save()

      event.traded += int(quote)
      event.unmatched_bets -=1
      event.matched_bets +=1
      event.save()

      return Response(data)
