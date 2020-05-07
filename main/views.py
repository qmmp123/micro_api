from django.contrib.auth import authenticate
from django.http import HttpRequest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import logging

logger = logging.getLogger(__name__)


# Create your views here.


@api_view(['POST'])
def register(request: HttpRequest):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    logger.warning(request.POST)
    if not username or not password or not email:
        return Response({"msg": "Params are necessary"})
    user = User.objects.filter(username=username).first()
    if user:
        return Response({"error": "user with this nickname exists"})
    user = User()
    user.username = username
    user.set_password(password)
    user.email = email
    user.save()
    token = Token.objects.create(user=user)
    return Response({"msg": f"Your token is {token.key}"})


@api_view(['POST'])
def get_token(request: HttpRequest):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:
        return Response({"msg": "Params are necessary"})
    user = authenticate(username=username, password=password)
    if user is not None:
        token = Token.objects.filter(user=user).first()
        return Response({"msg": f"Your token is {token.key}"})
    else:
        return Response({"msg": "Incorrect username or password"})
