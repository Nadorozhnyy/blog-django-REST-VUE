from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from users.models import UserProfile
from users.serializers import UserProfileSerializer


class UserProfileViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
