from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import action
#Permissions
from rest_framework.permissions import (
  AllowAny,
  IsAuthenticated
)
#Serializers
from cride.matches.serializers import RequestModelSerializer
from cride.users.serializers import UserModelSerializer
#models
from cride.users.models import User
from cride.matches.models import Request

class RequestViewSet(mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
  """User view set"""
  """Handle Login, SignUp y verification"""


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
        queryset = Request.objects.all()
        back_user = self.request.query_params.get('back_user')
        back_team = self.request.query_params.get('back_team')
        event = self.request.query_params.get('event')

        # queryset = queryset.filter(
        #   back_team= back_team
        # )

        return queryset
  # def create(request, *args, **kwargs):
  #     """Asign circle admin"""
  #     user = self.request.user
  #     team = self.request.team
  #     amount = self.request.amount
  #     event = self.request.event

  #     Request.objects.create(
  #       back_user = user,
  #       event= event,
  #       amount = amount,
  #       team = team
  #     )


  # def retrieve(self, request, *args, **kwargs):
  #     response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
  #     data = {
  #       "user": response.data,
  #     }
  #     response.data = data
  #     return response
