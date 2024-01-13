from rest_framework import serializers
from blog.models import BlogPost, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "user", "blog_post", "content", "created_date")
        read_only_fields = ("blog_post", "user", "created_date",)


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ("id", "author", "title", "content")
        read_only_fields = ("author", "created_date")


class BlogPostRetrieveSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ("id", "author", "title", "content", "comments")
        read_only_fields = ("created_date", "author")

    @staticmethod
    def get_comments(obj):
        comments_queryset = Comment.objects.filter(blog_post=obj.id)
        return CommentSerializer(comments_queryset, many=True).data

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
