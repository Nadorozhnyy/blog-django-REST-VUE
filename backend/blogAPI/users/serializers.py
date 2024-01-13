from djoser.serializers import UserCreateSerializer, User
from django.db import transaction
from djoser.conf import settings
from django.contrib.auth.models import Group


def add_user_to_group(user):
    my_group = Group.objects.get(name='users')
    my_group.user_set.add(user)


class CustomUserCreateMixin(UserCreateSerializer):

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        add_user_to_group(user)
        return user
