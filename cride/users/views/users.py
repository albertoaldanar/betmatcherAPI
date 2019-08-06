from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from django.db.models import Q
#Permissions
from rest_framework.permissions import (
  AllowAny,
  IsAuthenticated
)
#Serializers
from users.serializers import (
  UserLoginSerializer,
  UserModelSerializer,
  UserSignUpSerializer,
  AccountVerificationSerializer
)
from cride.matches.serializers import RequestModelSerializer
from cride.betfriends.serializers import BetFriendModelSerializer
#models
from cride.users.models import User
from cride.matches.models import Request
from cride.betfriends.models import BetFriend, FriendRequest

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
  """User view set"""
  """Handle Login, SignUp y verification"""

  queryset = User.objects.filter(is_active = True)
  serializer_class = UserModelSerializer
  lookup_field = "username"

  def get_permissions(self):
    """Asign Permission based on action"""
    if self.action in ["signup", "login", "verify"]:
        permissions = [AllowAny]
    elif self.action == ["retrieve", "update", "partial_update"]:
        permissions = [IsAuthenticated, IsAccountOwner]
    else:
        permissions = [IsAuthenticated]
    return [p() for p in permissions]

  @action(detail=False, methods=['post'])
  def login(self, request):
      serealizer = UserLoginSerializer(data = request.data)
      serealizer.is_valid(raise_exception =True)
      user, token = serealizer.save()

      data = {
        "user": UserModelSerializer(user).data,
        "jwt": token
      }
      return Response(data, status = status.HTTP_201_CREATED)


  @action(detail=False, methods=["post"])
  def signup(self, request):
      serealizer = UserSignUpSerializer(data = request.data)
      serealizer.is_valid(raise_exception =True)
      user, jwt = serealizer.save()
      data = {
        "user": UserModelSerializer(user).data,
        "jwt": jwt
      }
      return Response(data, status = status.HTTP_201_CREATED)


  @action(detail=False, methods=["post"])
  def verify(self, request):
      serealizer = AccountVerificationSerializer(data = request.data)
      serealizer.is_valid(raise_exception =True)
      serealizer.save()

      data = {"message": "Congratulations now go to the app"}

      return Response(data, status = status.HTTP_200_OK)

  # @action(detail =True, methods = ["put", "patch"])
  # def profile(self, request, *args, **kwargs):
  #     user = self.get_object()
  #     profile = user.profile
  #     partial = request.method == "PATCH"
  #     serializer = ProfileModelSerializer(
  #       profile,
  #       data = request.data,
  #       partial= partial
  #     )
  #     serializer.is_valid(raise_exception = True)
  #     serializer.save()
  #     data = UserModelSerializer(user).data
  #     return Response(data)

  def retrieve(self, request, *args, **kwargs):
      response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
      data = {
        "user": response.data,
      }
      response.data = data
      return response


@api_view(["GET"])
def user_info(request):
      opponent_param = request.query_params.get("user")
      current_user_param = request.query_params.get("current_user")

      opponent = User.objects.get(username = opponent_param)
      current_user = User.objects.get(username = current_user_param)

      try:
          friend = BetFriend.objects.get(Q(Q(user_a = opponent) & Q(user_b = current_user)) | Q(Q(user_a = current_user) & Q(user_b = opponent)))
      except BetFriend.DoesNotExist:
          friend = None

      result = True if friend else False
      # if result!= True:
      #   try:
      #     requested = FriendRequest.objects.get(Q(Q(sent_by = opponent) & Q(received_by = current_user)) | Q(Q(sent_by = current_user) & Q(received_by = opponent)))
      #   except FriendRequest.DoesNotExist:
      #     requested = None

      #   result = "Wating" if requested else False

      data = {
        "user": UserModelSerializer(opponent).data,
        "result": result
      }

      return Response(data)

@api_view(["GET"])
def user_live(request):
      # get http request params
      user_param = request.query_params.get("user")
      current_user_param = request.query_params.get("current_user")

      #filter users
      if user_param :
        users = User.objects.filter(Q(username__icontains = user_param), ~Q(username = current_user_param)).values()
      else:
        users = User.objects.filter(username = current_user_param)

      data = {
        "users": UserModelSerializer(users, many = True).data,
      }

      return Response(data)

