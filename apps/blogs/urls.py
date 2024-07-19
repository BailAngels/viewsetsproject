from rest_framework.routers import DefaultRouter

from apps.blogs import views

router = DefaultRouter()
router.register('blog',views.BlogViewSet,basename='blog')
router.register('image',views.BlogImageViewSet,basename='image')

urlpatterns = [
]

urlpatterns += router.urls
