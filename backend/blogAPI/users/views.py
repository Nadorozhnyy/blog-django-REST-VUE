from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from users.models import CustomUser
from users.serializers import UserSerializer, UserGroupSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class UserProfileViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserGroupView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_groups = request.user.groups.all()
        serializer = UserGroupSerializer(user_groups, many=True)
        return Response(serializer.data)
