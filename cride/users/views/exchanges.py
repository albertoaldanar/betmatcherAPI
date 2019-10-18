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
def shipment_exchange(request):
    exchange = Exchange.objects.get(id = request.data["exchange"])

    exchange.phone = request.data["phone"]
    exchange.email = request.data["email"]
    exchange.adress = request.data["adress"]
    exchange.country = request.data["country"]
    exchange.state = request.data["state"]
    exchange.city = request.data["city"]
    exchange.cp = request.data["cp"]
    exchange.full_name = request.data["full_name"]

    exchange.save()

    data = {"Exchange": ExchangeModelSerializer(exchange).data}

    return Response(data)