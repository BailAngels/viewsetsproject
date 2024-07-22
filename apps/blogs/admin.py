from django.contrib import admin

from apps.blogs.models import Blog, BlogImage,BlogFavorite


admin.site.register(Blog)
admin.site.register(BlogImage)
admin.site.register(BlogFavorite)
