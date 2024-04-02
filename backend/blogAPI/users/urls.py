from django.urls import path, include
from rest_framework import routers

from users.views import UserProfileViewSet, UserGroupView

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('<int:pk>', UserProfileViewSet.as_view({'get': 'retrieve'}), name='users_retrieve'),
    path('my_group', UserGroupView.as_view(), name='user-groups'),
]