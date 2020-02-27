from . import serializers
from .. import models
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        if username is not None and password is not None:
            # user_obj = models.BaseUser.objects.filter(username=username)
            user_obj = authenticate(username=username, password=password)
            if user_obj is not None and user_obj.is_active:
                login(self.request, user_obj)
            # if user_obj.exists() and user_obj.first().check_password(password):
                user = serializers.UserLoginSerializer(user_obj)
                data_list = {}
                data_list.update(user.data)
                data_list['token'] = Token.objects.get(user=user.instance).key
                return Response({"message": "Login Successfully", "data": data_list, "code": 200})
            else:
                message = "Unable to login with given credentials"
                return Response({"message": message, "code": 500, 'data': {}})
        else:
            message = "Invalid login details."
            return Response({"message": message, "code": 500, 'data': {}})


@api_view(['POST'])
@permission_classes([AllowAny])
def registration_api_view(request):
    if request.method == 'POST':
        serializer = serializers.RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully registered.'
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)


