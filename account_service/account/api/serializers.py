from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import fields
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ValidationError

User = get_user_model()


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "type",
            "password",
            "is_staff",
            "is_superuser",
        ]
        extra_kwargs = {
            "email": {
                "required": True,
            },
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "type"]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "required": True,
            },
            "email": {
                "required": True,
            },
        }


class LoginSerializer(serializers.Serializer):
    email = fields.CharField(required=True, max_length=120, help_text="User's email")
    password = fields.CharField(
        required=True, max_length=120, help_text="User's password"
    )


class PasswordResetSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    password = serializers.CharField(max_length=255, help_text="password")
    confirm_password = serializers.CharField(
        max_length=255, help_text="confirm password"
    )

    class Meta:
        extra_kwargs = {
            "password": {"required": True},
            "confirm_password": {"required": True},
        }

    def validate_user(self, value):
        user = User.objects.get(id=value)

        if user:
            return user

        raise serializers.ValidationError({"user": "user does not exists"})

    def validated_password(self, value):
        if len(value < 8):
            raise serializers.ValidationError(
                {"user": "password length must be atleast 8 chars"}
            )
        return value

    def validated_confirm_password(self, value):
        if len(value < 8):
            raise serializers.ValidationError(
                {"user": "confirm password length must be atleast 8 chars"}
            )
        return value

    def create(self, validated_data):
        # data = validated_data

        if validated_data.get("password", None) != validated_data.get(
            "confirm_password", None
        ):
            raise serializers.ValidationError(
                {"confirm_password": "confirm password don't match"}
            )

        validated_data["user"].set_password(validated_data.get("password"))


class UpdatePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=120, help_text="old password")
    new_password = serializers.CharField(max_length=120, help_text="new password")
    confirm_password = serializers.CharField(
        max_length=120, help_text="confirmation of the new password"
    )

    class Meta:
        extra_kwargs = {
            "old_password": {"required": True},
            "new_password": {"required": True},
            "confirm_password": {"required": True},
        }
