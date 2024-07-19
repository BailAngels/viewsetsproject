from rest_framework import viewsets

from django.contrib.auth import get_user_model

from apps.users import serializers


User = get_user_model()


class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.SignUpSerializer
        return self.serializer_class
