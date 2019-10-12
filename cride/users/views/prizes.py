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
from cride.users.serializers import PrizeModelSerializer
#Utilities
from heapq import nlargest
#Models
from cride.users.models import Prize, User, Exchange


@api_view(["POST"])
def pay_prize(request):
    current_user = User.objects.get(username = request.data["current_user"])
    prize = Prize.objects.get(name = request.data["prize"])

    date = request.data["date"]

    response = Exchange.objects.create(
        user = current_user,
        prize = prize, 
        date = date
    )

    data = {"Exchange": ExchangeModelSerializer(response).data}

    current_user.profile.coins -= prize.price
    current_user.save()

    return Response(data)
