from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

__all__ = [
    "EmailSerializer",
    "PasswordTokenSerializer",
    "TokenSerializer",
]


class EmailSerializer(serializers.Serializer):
    # This field can contains either a username or an email
    # but for backward compatibility the field name is kept.
    email = serializers.CharField()


class PasswordTokenSerializer(serializers.Serializer):
    password = serializers.CharField(
        label=_("Password"), style={"input_type": "password"}
    )
    token = serializers.CharField()


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()
