from rest_framework import viewsets

from apps.tags.models import Tag
from apps.tags.serializers import TagSerializer


class TagAPIView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
