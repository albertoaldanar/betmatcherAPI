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
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet,
                    APIView):
  """Request view set"""

  serializer_class = RequestModelSerializer

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

@api_view(["GET"])
def users_to_match(request):
      back_user = request.query_params.get("back_user")
      user = User.objects.get(username = back_user)

      back_team = request.query_params.get("back_team")
      event = request.query_params.get("event")
      reqs = Request.objects.filter(
          ~Q(back_team = back_team),
          ~Q(back_user__username = back_user),
          is_public = True,
          is_matched = False,
          event__name = event,
      )
      
      data = {
        "reqs": RequestModelSerializer(reqs, many = True).data, 
        "user": UserModelSerializer(user).data,
      }

      return Response(data)


@api_view(["POST"])
def post_request(request):
      back_user = User.objects.get(username = request.data["back_user"])
      event = Event.objects.get(name = request.data["event"])

      b = back_user.profile

      response = Request.objects.create(
        back_user = back_user,
        event = event,
        amount = request.data["amount"],
        back_team = request.data["back_team"],
        is_public = request.data["is_public"],
        opponent = request.data["opponent"],
        fq = request.data["fq"],
        sq = request.data["sq"],
        fq_position = request.data["fq_position"],
        sq_position = request.data["sq_position"],
      )

      data = {"request": RequestModelSerializer(response).data}

      event.traded += int(request.data["amount"])
      event.unmatched_bets += 1
      event.save()

      b.coins -= int(request.data["amount"])
      b.save()
      return Response(data)


@api_view(["GET"])
def direct_bets(request):
    current_user = self.request.query_params.get("current_user")

    direct_bets = Request.objects.filter(opponent = current_user, is_public = False)

    data = {"direct_bets": RequestModelSerializer(direct_bets).data}

    return Response(data)


@api_view(["POST"])
def decline_bet(request):
    bet_request = Request.objects.get(id = request.data["declined_id"])
    bet_request.declined = True

    bet_request.save()

    return Response("Updated")


@api_view(["DELETE"])
def cancel_request(request):
    req = Request.objects.get(id = request.data["req"])
    req.delete()

    user = req.back_user.profile
    user.coins += req.amount
    user.save()

    return Response("Deleted!")
