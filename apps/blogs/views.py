from rest_framework import viewsets,permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.blogs.models import Blog,BlogImage,BlogFavorite
from apps.blogs import serializers
from apps.blogs.permissions import IsAdminOrOwnerPermission


class BlogAPIView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [IsAdminOrOwnerPermission]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        'author','tag'
    ]
    search_fields = [
        'author__username','title',
    ]
    ordering_fields = [ 
        'author','title',
    ] 


    def get_serializer_class(self):
        if self.action in ['create','update']:
            return serializers.BlogCreateUpdateSerializer
        elif self.action in ['retrieve']:
            return serializers.BlogRetrieveSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        return serializer.save(author = self.request.user)
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticatedOrReadOnly()]
        return [permission() for permission in self.permission_classes]
    
    
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