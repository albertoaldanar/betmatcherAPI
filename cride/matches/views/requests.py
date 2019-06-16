from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import action
#Django
from django.db.models import Q
#Permissions
from rest_framework.permissions import (
  AllowAny,
  IsAuthenticated
)
#Serializers
from cride.matches.serializers import RequestModelSerializer, CreateRequestSerializer
from cride.users.serializers import UserModelSerializer
#models
from cride.users.models import User
from cride.matches.models import Request
from cride.events.models import Event

class RequestViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
  """Request view set"""

  serializer_class = RequestModelSerializer
  # def get_permissions(self):
  #   """Asign Permission based on action"""
  #   if self.action in ["signup", "login", "verify"]:
  #       permissions = [AllowAny]
  #   elif self.action == ["retrieve", "update", "partial_update"]:
  #       permissions = [IsAuthenticated, IsAccountOwner]
  #   else:
  #       permissions = [IsAuthenticated]
  #   return [p() for p in permissions]

  def get_queryset(self):
        back_user = self.request.query_params.get("back_user")
        back_team = self.request.query_params.get("back_team")
        event = self.request.query_params.get("event")

        queryset = Request.objects.filter(
          ~Q(back_team = back_team),
          ~Q(back_user__username = back_user),
          is_public = True,
          is_matched = False,
          event__name = event,
        )
        return queryset

  #     """Asign circle admin"""

  # def create(self, request):

  #   back_user = request.back_user
  #   back_team = request.back_team
  #   amount = request.amount
  #   event = request.event

  #   r = Request.objects.create(
  #     back_user = back_user,
  #     event = event,
  #     amount = amount,
  #     back_team = back_team,
  #   )

  #   return r

  # def create(self, request, *args, **kwargs):

  #   back_user = request.back_user
  #   back_team = request.back_team
  #   amount = request.amount
  #   event = request.event

  #   response = Request.objects.create(
  #     back_user__username = back_user,
  #     event__name = event,
  #     amount = amount,
  #     back_team = back_team,
  #   )

  #   return Response(RequestModelSerializer(response.data))

@api_view(["POST"])
def post_request(request):
      # serializer = CreateRequestSerializer(data = request.data)
      # serializer.is_valid(raise_exception = True)
      # data = serializer.data

      # req = serializer.save()
      back_user = User.objects.get(username = request.data["back_user"])
      event = Event.objects.get(name = request.data["event"])

      b = back_user.profile

      response = Request.objects.create(
        back_user = back_user,
        event = event,
        amount = request.data["amount"],
        back_team = request.data["back_team"],
        is_public = request.data["is_public"]
      )

      data = {"request": RequestModelSerializer(response).data}

      event.traded += int(request.data["amount"])
      event.unmatched_bets += 1
      event.save()

      b.coins -= int(request.data["amount"])
      b.save()

      return Response(data)

