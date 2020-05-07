from typing import Optional

from django.contrib.auth import authenticate
from django.http import HttpRequest
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import logging

from main.models import AppModel
from main.serializers import AppModelSerializer

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


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_app(request: HttpRequest):
    name = request.POST.get('name')
    if not name:
        return Response({"msg": "Cannot create app without name"})
    app = AppModel()
    app.name = name
    app.save()
    return Response({"msg": f"Successfully api key for an app is {app.api_key}"})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def change_app(request: HttpRequest):
    api_key = request.POST.get("api_key")
    additional_info = request.POST.get('info')
    name = request.POST.get('name')
    if not api_key:
        return Response({"Error": "cannot change without api_key"})
    app: Optional[AppModel] = AppModel.objects.filter(api_key=api_key).first()
    if not app:
        return Response({"error": "App with this api key does not exists"})
    if not additional_info:
        additional_info = app.additional_info
    if not name:
        name = app.additional_info
    app.additional_info = additional_info
    app.name = name
    app.save()
    return Response({"msg": "Info updated successfully"})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_app(request: HttpRequest):
    api_key = request.POST.get("api_key")
    if not api_key:
        return Response({"Error": "cannot delete without api_key"})
    app: Optional[AppModel] = AppModel.objects.filter(api_key=api_key).first()
    if not app:
        return Response({"error": "App with this api key does not exists"})
    app.delete()
    return Response({"msg": "App has been removed successfully"})


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_info(request: HttpRequest):
    api_key = request.POST.get("api_key")
    if not api_key:
        return Response({"Error": "cannot change without api_key"})
    app: Optional[AppModel] = AppModel.objects.filter(api_key=api_key).first()
    if not app:
        return Response({"error": "App with this api key does not exists"})
    serializer = AppModelSerializer(app)
    return Response(serializer.data)
