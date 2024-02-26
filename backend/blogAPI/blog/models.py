from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser as Profile


class BlogPost(models.Model):
    author = models.ForeignKey(Profile, related_name="blogposts", verbose_name=_("post author"),
                               on_delete=models.CASCADE)
    title = models.TextField(max_length=100, verbose_name=_("title"))
    content = models.TextField(max_length=5000, verbose_name=_("blog post"))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("created date"))

    def __str__(self):
        return str(self.title[:50])


class Comment(models.Model):
    user = models.ForeignKey(Profile, related_name="users", verbose_name=_("commentary author"),
                             on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, related_name='comments', verbose_name=_("blog post"),
                                  on_delete=models.CASCADE)
    content = models.TextField(max_length=1000, verbose_name=_("comment"))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("created date"))

    def __str__(self):
        return str(self.content[:50])
