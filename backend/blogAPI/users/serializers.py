from djoser.serializers import UserCreateSerializer, User
from rest_framework import serializers
from django.db import transaction
from djoser.conf import settings
from django.contrib.auth.models import Group
from users.models import CustomUser


def add_user_to_group(user):
    my_group = Group.objects.get(name='users')
    my_group.user_set.add(user)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email")


class CustomUserCreateMixin(UserCreateSerializer):

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        add_user_to_group(user)
        return user


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name")
