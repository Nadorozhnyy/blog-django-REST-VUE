from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from users.models import CustomUser
from users.serializers import UserProfileSerializer


class UserProfileViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
