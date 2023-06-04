from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
)
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.authentication import TokenAuthentication
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model, authenticate, logout, login
from rest_framework import status
from django.http import JsonResponse, request
from rest_framework.authtoken.models import Token
from .serializers import (
    LoginSerializer,
    UserSerializer,
    UpdatePasswordSerializer,
    PasswordResetSerializer,
)

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView

User = get_user_model()


class LoginViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            token = user.auth_token.key
            context = {
                "token": token,
            }
            return Response(context)
        else:
            return Response(
                {"detail": "email or password invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserViewSet(
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == "POST":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        return UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
        Token.objects.create(user=instance)
        return Response(UserSerializer(instance).data, status=201)

    def update(self, request, *args, **kwargs):
        instance: User = self.get_object()
        user = self.get_user()
        if instance.user == user:
            return super().update(request, *args, **kwargs)
        return JsonResponse({"detail": "you are nor allow to update this user_profile"})

    def partial_update(self, request, *args, **kwargs):
        instance: User = self.get_object()
        user = self.get_user()
        if instance.user == user:
            return super().partial_update(request, *args, **kwargs)
        return Response({"detail": "you are not allow to update this user_profile"})


class UserExistsViewSet(GenericViewSet, ListAPIView):
    def get(self, request, *args, **kwargs):
        email = request.query_params.get("email")
        if email:
            user = User.objects.get(email=email)
            serializer = UserSerializer(user)
            if user:
                Response(
                    {"found": True, "user": serializer.data}, status=status.HTTP_200_OK
                )
            return Response({"found": False}, status=status.HTTP_404_NOT_FOUND)

        return Response({"found": False}, status=status.HTTP_404_NOT_FOUND)


class ValidateTokenView(GenericViewSet, ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return Response(
            {"data": "valid token", "user": request.user}, status=status.HTTP_200_OK
        )


class ResetPasswordView(GenericViewSet, CreateAPIView):
    permission_classes = [AllowAny]

    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({"success": True})


class UpdatePasswordViewSet(GenericViewSet, CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        confirm_password = request.data.get("confirm_password")

        if not request.user.check_password(old_password):
            return Response(
                {"success": False, "message": "old password don't match"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if len(new_password) < 8:
            return Response(
                {
                    "success": False,
                    "message": "password is too short require atleast 8 characters",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if new_password != confirm_password:
            return Response(
                {"success": False, "message": "password don't match"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = request.user
        user.set_password(new_password)
        user.save()

        if user.check_password(new_password):
            return Response(
                {"message": "password updated successfully", "success": True},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Something went wrong", "success": False},
                status=status.HTTP_400_BAD_REQUEST,
            )
