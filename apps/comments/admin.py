from django.contrib import admin

from apps.comments.models import Comment,CommentFavorite


admin.site.register(Comment)
admin.site.register(CommentFavorite)
