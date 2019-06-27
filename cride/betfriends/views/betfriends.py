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
from cride.users.models import User

# class FriendRequestViewSet(mixins.CreateModelMixin,
#                     mixins.ListModelMixin,
#                     mixins.DestroyModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     viewsets.GenericViewSet):
#   """Event view set"""

#   serializer_class = FriendRequestModelSerializer

#   def get_object(self, notepad_pk):
#     try:
#         return FriendRequest.objects.get(pk=notepad_pk)
#     except Notepad.DoesNotExist:
#         raise Http404

#   def delete(self, request, notepad_pk, format=None):
#     item = self.get_object(notepad_pk)
#     item.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(["POST"])
def create_friendship(request):
      friend_request = FriendRequest.objects.get(id = request.data["friend_request"])
      current_user = User.objects.get(username = request.data["current_user"])

      betfriends = BetFriend.objects.create(user_a = friend_request.sent_by, user_b = current_user)

      friend_request.is_accepted = True
      friend_request.save()

      data = {
        "friendship": BetFriendModelSerializer(betfriends).data,
      }
      return Response(data)

@api_view(["DELETE"])
def decline_request(request):
      friend_request = FriendRequest.objects.get(id = request.data["friend_request"])
      friend_request.delete()
      data = {
        "friendship": "OK",
      }
      return Response(data)


@api_view(["GET"])
def betfriends_data(request):
      current_user = request.query_params.get("current_user")
      betfriends = BetFriend.objects.filter(Q(user_a__username = current_user) | Q(user_b__username = current_user)).order_by("created")
      friend_requests = FriendRequest.objects.filter(received_by__username = current_user, is_accepted = False).order_by("created")

      data = {
        "betfirends": BetFriendModelSerializer(betfriends, many= True).data,
        "friend_requests": FriendRequestModelSerializer(friend_requests, many= True).data,
      }
      return Response(data)
