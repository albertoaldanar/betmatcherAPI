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
from cride.users.serializers import PrizeModelSerializer, ExchangeModelSerializer
#Utilities
from heapq import nlargest
#Models
from cride.users.models import Prize, User, Exchange


@api_view(["POST"])
def pay_prize(request):
    current_user = User.objects.get(username = request.data["current_user"])
    prize = Prize.objects.get(name = request.data["prize"])

    user_coins = current_user.profile

    date = request.data["date"]
    coins = request.data["coins"]

    user_coins.coins -= prize.price
    user_coins.save()

    response = Exchange.objects.create(
      user = current_user,
      prize = prize, 
      date = date
    )

    data = {"Exchange": ExchangeModelSerializer(response).data}

    return Response(data)


@api_view(["GET"])
def get_all_prizes(request):

    response = Prize.objects.all()
    data = {"prizes": PrizeModelSerializer(response, many= True).data}

    return Response(data)

