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

@api_view(["GET"])
def matches(request):

      permission_classes = (IsAuthenticated,)

      unmatched_bets = Request.objects.filter(
        is_matched = False,
        back_user = request.user
      ).order_by("created")

      matches = Match.objects.filter(Q(back_user = request.user) | Q(lay_user = request.user)).order_by("created")

      matched_bets = matches.filter(is_finished = False)
      finished_bets = matches.filter(is_finished = True)

      data = {
        "unmatched_bets": RequestModelSerializer(unmatched_bets, many= True).data,
        "matched_bets": MatchModelSerializer(matched_bets, many= True).data,
        "finished_bets": MatchModelSerializer(finished_bets, many= True).data,
      }

      return Response(data)

# class MatchesViewSet(mixins.CreateModelMixin,
#                     mixins.ListModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     viewsets.GenericViewSet):

#     # serializer_class = RequestModelSerializer
#     # permission_classes = (IsAuthenticated,)

#     # def get_queryset(self):
#     #   queryset = Request.objects.filter(is_matched = False)
#     #   # serializer2 = UserModelSerializer(matches, many=True)
#     #   data = {
#     #     "top_requests": RequestModelSerializer(queryset, many=True)
#     #   }
#     #   return Response(data)

