from rest_framework.routers import DefaultRouter

from apps.blogs.api import views

router = DefaultRouter()
router.register('blog',views.BlogAPIView,basename='blog')
router.register('image',views.BlogImageAPIView,basename='image')
router.register('like',views.BlogLikeAPIView,basename='like')

urlpatterns = [
]

urlpatterns += router.urls
