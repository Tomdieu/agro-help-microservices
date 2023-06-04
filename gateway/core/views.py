from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from django.conf import settings

from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

import requests

from .serializers import (
    UserSerializer,
    LoginSerializer,
    SuccessSerializer,
    TokenSerializer,
    PasswordResetSerializer,
    UpdatePasswordSerializer,
    # Culture Serializers
    CultureSerializer,
    SoilSerializer,
    CultureDiseaseSerializer,
    CultureWithPracticeSerializer,
)

# Create your views here.


class LoginView(APIView):
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response(
                "Authentication Response", TokenSerializer
            )
        },
    )
    def post(self, request, *args, **kwargs):
        data = request.data

        print(f"URL = {settings.ACCOUNT_SERVICE}/api/account/auth/")

        response = requests.post(
            f"{settings.ACCOUNT_SERVICE}/api/account/auth/", data=data
        )
        # return Response("token")
        return Response(response.json(), status=response.status_code)


class UserViewList(APIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(
        responses={200: openapi.Response("User Response", UserSerializer)}
    )
    def get(self, request, *args, **kwargs):
        token = request.headers.get("Authorization")
        print(f"{settings.ACCOUNT_SERVICE}/api/account/user/")
        response = requests.get(
            f"{settings.ACCOUNT_SERVICE}/api/account/user/",
            headers={"Content-Type": "application/json", "Authorization": token},
        )
        return Response(response.json(), status=response.status_code)

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request, *args, **kwargs):
        token = request.headers.get("Authorization")
        data = request.data
        response = requests.post(
            f"{settings.ACCOUNT_SERVICE}/api/account/user/",
            data=data,
            headers={"Content-Type": "application/json", "Authorization": token},
        )
        return Response(response.json(), status=response.status_code)


class UserViewDetail(APIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(
        responses={200: openapi.Response("User Response", UserSerializer)}
    )
    def get(self, request, pk, *args, **kwargs):
        print(pk)
        token = request.headers.get("Authorization")
        response = requests.get(
            f"{settings.ACCOUNT_SERVICE}/api/account/user/{pk}",
            headers={"Content-Type": "application/json", "Authorization": token},
        )
        return Response(response.json(), status=response.status_code)

    @swagger_auto_schema(
        responses={200: openapi.Response("User Response", UserSerializer)}
    )
    def patch(self, request, pk, *args, **kwargs):
        token = request.headers.get("Authorization")
        data = request.data
        response = requests.patch(
            f"{settings.ACCOUNT_SERVICE}/api/account/user/{pk}",
            data=data,
            headers={"Content-Type": "application/json", "Authorization": token},
        )
        return Response(response.json(), status=response.status_code)

    @swagger_auto_schema(
        responses={200: openapi.Response("User Response", UserSerializer)}
    )
    def put(self, request, pk, *args, **kwargs):
        token = request.headers.get("Authorization")
        data = request.data
        response = requests.put(
            f"{settings.ACCOUNT_SERVICE}/api/account/user/{pk}",
            data=data,
            headers={"Content-Type": "application/json", "Authorization": token},
        )
        return Response(response.json(), status=response.status_code)

    @swagger_auto_schema(responses={status.HTTP_204_NO_CONTENT: "Content Not Found"})
    def delete(self, request, pk, *args, **kwargs):
        token = request.headers.get("Authorization")
        response = requests.delete(
            f"{settings.ACCOUNT_SERVICE}/api/account/user/{pk}",
            headers={"Content-Type": "application/json", "Authorization": token},
        )
        return Response(response.json(), status=response.status_code)


class ValidateTokenView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.headers.get("Authorization")
        data = request.data
        response = requests.post(
            f"{settings.ACCOUNT_SERVICE}/api/account/validate-token/",
            data=data,
            headers={"Content-Type": "application/json", "Authorization": token},
        )
        return Response(response.json(), status=response.status_code)


class ResetPasswordView(APIView):
    @swagger_auto_schema(
        request_body=PasswordResetSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response(
                "Authentication Response", SuccessSerializer
            )
        },
    )
    def post(self, request, *args, **kwargs):
        token = request.headers.get("Authorization")
        data = request.data
        response = requests.post(
            f"{settings.ACCOUNT_SERVICE}/api/account/reset-password/",
            data=data,
            headers={"Content-Type": "application/json", "Authorization": token},
        )
        return Response(response.json(), status=response.status_code)


class UpdatePasswordView(APIView):
    @swagger_auto_schema(
        request_body=UpdatePasswordSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response(
                "Authentication Response", SuccessSerializer
            )
        },
    )
    def post(self, request, *args, **kwargs):
        token = request.headers.get("Authorization")
        data = request.data
        response = requests.post(
            f"{settings.ACCOUNT_SERVICE}/api/account/updated-password/",
            data=data,
            headers={"Content-Type": "application/json", "Authorization": token},
        )
        return Response(response.json(), status=response.status_code)


# Cultures View
# class CultureView(APIView):
#     @swagger_auto_schema(
#         responses={
#             status.HTTP_200_OK: openapi.Response(
#                 description="List of cultures",
#                 schema=openapi.Schema(type=openapi.TYPE_ARRAY, items=CultureSerializer),
#             )
#         }
#     )
#     def get(self, request, *args, **kwargs):
#         token = request.headers.get("Authorization")
#         data = request.data
#         response = requests.get(
#             f"{settings.CULTURE_SERVICE}/api/culture/",
#             data=data,
#             headers={"Content-Type": "application/json", "Authorization": token},
#         )
#         return Response(response.json(), status=response.status_code)


class CultureViewSet(ViewSet):
    # @swagger_auto_schema(
    #     responses={
    #         status.HTTP_200_OK: openapi.Response(
    #             description="List of cultures", schema=CultureSerializer
    #         )
    #     }
    # )
    def list(self, request, *args, **kwargs):
        token = request.headers.get("Authorization")
        data = request.data
        response = requests.get(
            f"{settings.CULTURE_SERVICE}/api/culture/",
            data=data,
            headers={"Content-Type": "application/json", "Authorization": token},
        )
        return Response(response.json(), status=response.status_code)

    # @swagger_auto_schema(
    #     responses=openapi.Response(
    #         description="Get a culture", schema=CultureSerializer
    #     )
    # )
    def retrieve(self, request, pk=None, *args, **kwargs):
        token = request.headers.get("Authorization")
        data = request.data
        response = requests.get(
            f"{settings.CULTURE_SERVICE}/api/culture/{pk}/",
            data=data,
            headers={"Content-Type": "application/json", "Authorization": token},
        )
        return Response(response.json(), status=response.status_code)

    # @swagger_auto_schema(
    #     responses=openapi.Response(
    #         description="Get List of culture diseases",
    #         schema=openapi.Schema(
    #             type=openapi.TYPE_ARRAY, items=CultureDiseaseSerializer
    #         ),
    #     )
    # )
    @action(methods=["GET"], detail=True)
    def disease(self, request, pk=None, *args, **kwargs):
        token = request.headers.get("Authorization")
        data = request.data
        response = requests.get(
            f"{settings.CULTURE_SERVICE}/api/culture/{pk}/disease/",
            data=data,
            headers={"Content-Type": "application/json", "Authorization": token},
        )
        return Response(response.json(), status=response.status_code)

    @swagger_auto_schema(
        responses=openapi.Response(
            description="Get List of culture practise",
            schema=CultureWithPracticeSerializer,
        )
    )
    @action(methods=["GET"], detail=True)
    def practise(self, request, pk=None, *args, **kwargs):
        token = request.headers.get("Authorization")
        data = request.data
        response = requests.get(
            f"{settings.CULTURE_SERVICE}/api/culture/{pk}/practise/",
            data=data,
            headers={"Content-Type": "application/json", "Authorization": token},
        )
        return Response(response.json(), status=response.status_code)
