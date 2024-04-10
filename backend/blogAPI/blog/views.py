from django.http import HttpResponseRedirect
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.reverse import reverse
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users.models import CustomUser
from blog.models import BlogPost, Comment
from blog.serializers import BlogPostSerializer, CommentSerializer, BlogPostRetrieveSerializer
from blog.permissions import IsAdminOrReadOnly


class BlogPostPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    page_query_param = 'page'
    max_page_size = 100


class BlogPostViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = BlogPost.objects.all().order_by('-created_date')
    serializer_class = BlogPostSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = BlogPostPagination

    def perform_create(self, serializer):
        author = CustomUser.objects.get(id=self.request.user.id)
        serializer.save(author=author)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BlogPostRetrieveSerializer
        return BlogPostSerializer


class CommentViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(blog_post=BlogPost.objects.get(id=pk))

    def create(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        profile = CustomUser.objects.get(id=self.request.user.id)
        blog_post = BlogPost.objects.get(id=pk)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=profile, blog_post=blog_post)
        self.perform_create(serializer)
        return HttpResponseRedirect(redirect_to=reverse('blogposts_retrieve', args=[pk], request=request))
