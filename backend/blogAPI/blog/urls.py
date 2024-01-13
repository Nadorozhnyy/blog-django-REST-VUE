from django.urls import path, include
from rest_framework import routers

from .views import BlogPostViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register(r'blogpost', BlogPostViewSet)

urlpatterns = [
    path('blogposts/', BlogPostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('blogposts/<int:pk>', BlogPostViewSet.as_view({'get': 'retrieve'}), name='blogposts_retrieve'),
    path('blogposts/<int:pk>/create_comment', CommentViewSet.as_view({'post': 'create'}), ),
]