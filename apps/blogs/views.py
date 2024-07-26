from django.views import generic

from apps.blogs.models import Blog
from apps.blogs.forms import BlogForm


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blogs'