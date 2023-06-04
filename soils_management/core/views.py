from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
)
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model, authenticate, logout, login
from rest_framework import status
from django.http import JsonResponse, request
from rest_framework.authtoken.models import Token

from .serializers import (
    SoilAreaSerializer,
    SoilSerializer,
    SoilAreaSerializerCreate,
    SoilSerializerCreate,
)

from .models import SoilArea, Soil

# Create your views here.


class SoilAreaViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = SoilArea.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method.upper() in ["POST", "PUT", "PATCH"]:
            return SoilAreaSerializerCreate
        else:
            return SoilAreaSerializer


class SoilViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = Soil.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method.upper() in ["POST", "PUT", "PATCH"]:
            return SoilSerializerCreate
        else:
            return SoilSerializer
