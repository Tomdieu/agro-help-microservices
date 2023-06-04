from rest_framework import serializers
from rest_framework import fields


class TokenSerializer(serializers.Serializer):
    token = fields.CharField(max_length=255)


class UserSerializer(serializers.Serializer):
    USER_TYPES = (("agriculteur", "agriculteur"), ("expert", "expert"))
    username = fields.CharField(max_length=120)
    email = fields.EmailField(max_length=255)
    password = fields.CharField(max_length=255)
    type = fields.ChoiceField(choices=USER_TYPES)


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


class SuccessSerializer(serializers.Serializer):
    success = fields.BooleanField()


# Cultures Serializers


class _CultureSerializer(serializers.Serializer):
    name = fields.CharField(max_length=255)
    image = fields.ImageField()


class _SoilSerializer(serializers.ModelSerializer):
    name = fields.CharField(max_length=255)


class SoilSerializer(_SoilSerializer):
    cultures = _CultureSerializer(many=True)


class CultureSerializer(_CultureSerializer):
    soils = _SoilSerializer(many=True)


class CultureDiseaseSerializer(serializers.Serializer):
    disease_name = fields.CharField(max_length=255)
    solution = fields.CharField(max_length=30000)


class CultureWithPracticeSerializer(serializers.Serializer):
    name = fields.CharField(max_length=255)
    practise = fields.CharField(max_length=30000)
