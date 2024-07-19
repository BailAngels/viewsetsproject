from rest_framework.routers import DefaultRouter

from django.urls import path

from apps.tags import views

router = DefaultRouter()
router.register('tag', views.TagAPIView, basename='tag')

urlpatterns = [
]

urlpatterns += router.urls
