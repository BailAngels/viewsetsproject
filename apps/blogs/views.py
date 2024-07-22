from rest_framework import viewsets

from apps.blogs.models import Blog,BlogImage,BlogFavorite
from apps.blogs import serializers
from apps.blogs.permissions import IsAdminOrOwnerPermission


class BlogAPIView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [IsAdminOrOwnerPermission]

    def get_serializer_class(self):
        if self.action in ['create','update']:
            return serializers.BlogCreateUpdateSerializer
        elif self.action in ['retrieve']:
            return serializers.BlogRetrieveSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        return serializer.save(author = self.request.user)
    
    
class BlogImageAPIView(viewsets.ModelViewSet):
    queryset = BlogImage.objects.all()
    serializer_class = serializers.BlogImageSerializer


class BlogLikeAPIView(viewsets.ModelViewSet):
    queryset = BlogFavorite.objects.all()
    serializer_class = serializers.BlogLikeSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.BlogLikeCreateSeralizer
        return self.serializer_class
    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)