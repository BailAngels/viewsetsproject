from django.urls import path

from rest_framework.routers import DefaultRouter

from apps.comments import views


urlpatterns = [
]

router = DefaultRouter()
router.register('comment',views.CommentAPIView,basename='comment')

urlpatterns+=router.urls
