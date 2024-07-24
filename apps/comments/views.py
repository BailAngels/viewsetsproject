from rest_framework import viewsets

from apps.comments.models import Comment,CommentFavorite
from apps.comments import serializers


class CommentAPIView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.CommentCreateSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
    
class CommentLikeAPIView(viewsets.ModelViewSet):
    queryset = CommentFavorite.objects.all()
    serializer_class = serializers.CommentLikeSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.CommentLikeCreateSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)