from django.db import models
from django.contrib.auth import get_user_model

from apps.blogs.models import Blog 


User = get_user_model()


class Comment(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner',
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='blog',
    )

    def __str__(self):
        return self.owner
    
    