from django.urls import path

from rest_framework.routers import DefaultRouter

from apps.users import views

urlpatterns = [
]

router = DefaultRouter()
router.register('user', views.UserAPIView,basename='user')

urlpatterns+=router.urls
