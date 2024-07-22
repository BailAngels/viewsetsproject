from rest_framework import viewsets

from apps.comments.models import Comment
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