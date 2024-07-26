from django.urls import path

from apps.blogs import views

urlpatterns = [
    path('',views.BlogListView.as_view(),name='index')
]