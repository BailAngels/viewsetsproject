from rest_framework import viewsets

from apps.blogs.models import Blog,BlogImage
from apps.blogs.serializers import BlogImageSerializer,BlogSerializer,BlogCreateUpdateSerializer,BlogRetrieveSerializer
from apps.blogs.permissions import IsAdminOrOwnerPermission


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminOrOwnerPermission]

    def get_serializer_class(self):
        if self.action in ['create','update']:
            return BlogCreateUpdateSerializer
        elif self.action in ['retrieve']:
            return BlogRetrieveSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        return serializer.save(author = self.request.user)
    
    
class BlogImageViewSet(viewsets.ModelViewSet):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer