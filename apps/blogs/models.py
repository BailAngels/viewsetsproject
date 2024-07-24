from django.db import models
from django.contrib.auth import get_user_model

from apps.tags.models import Tag

User = get_user_model()


class Blog(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author'
    )
    title = models.CharField(
        max_length=150,
    )
    description = models.TextField(
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    tag = models.ManyToManyField(
        Tag,
        related_name='tag',
    )
    
    def __str__(self):
        return self.title


class BlogImage(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='blog_image',
    )
    photo = models.ImageField(
        upload_to='blog',
    )

    def __str__(self):
        return self.blog.title
    

class BlogFavorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='like_user',
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='like_blog',
    )

    def __str__(self):
        return self.user.username
    