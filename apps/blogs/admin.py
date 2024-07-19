from django.contrib import admin

from apps.blogs.models import Blog, BlogImage


admin.site.register(Blog)
admin.site.register(BlogImage)
