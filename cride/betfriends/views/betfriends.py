from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from django.db.models import Q

#Serializers
from cride.betfriends.serializers import FriendRequestModelSerializer, BetFriendModelSerializer
#models
from cride.betfriends.models import FriendRequest, BetFriend

# class LeaguesViewSet(mixins.CreateModelMixin,
#                     mixins.ListModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     viewsets.GenericViewSet):
#   """Event view set"""

#   serializer_class = LeagueModelSerializer

#   def get_queryset(self):
#         sport = self.request.query_params.get("sport")

#         queryset = League.objects.filter(
#           sport__name = sport,
#         )
#         return queryset
@api_view(["GET"])
def betfriends_data(request):
      current_user = User.objects.get(username = request.data["current_user"])
      betfriends = BetFriend.objects.filter(Q(user_a = current_user) | Q(user_b = current_user)).order_by("created")
      friend_requests = FriendRequest.objects.filter(Q(sent_by = current_user) | Q(received_by = current_user)).order_by("created")

      data = {
        "betfirends": BetFriendModelSerializer(betfriends, many= True).data,
        "friend_requests": FriendRequestModelSerializer(friend_requests, many= True).data,
      }
      return Response(data)