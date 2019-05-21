from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
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
from cride.users.models import User

@api_view(["POST"])
def login(request):
      serealizer = UserLoginSerializer(data = request.data)
      serealizer.is_valid(raise_exception =True)
      user, token = serealizer.save()

      data = {
        "user": UserModelSerializer(user).data,
        "acces_token": token
      }
      return Response(data, status = status.HTTP_201_CREATED)

@api_view(["POST"])
def signup(request):
      serealizer = UserSignUpSerializer(data = request.data)
      serealizer.is_valid(raise_exception =True)
      user = serealizer.save()
      data = UserModelSerializer(user).data

      return Response(data, status = status.HTTP_201_CREATED)


@api_view(["POST"])
def verify(request):
      serealizer = AccountVerificationSerializer(data = request.data)
      serealizer.is_valid(raise_exception =True)
      serealizer.save()

      data = {"message": "Congratulations now go to the app"}

      return Response(data, status = status.HTTP_200_OK)
