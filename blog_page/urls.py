from django.urls import path
from .views import index, post, post_detail

urlpatterns = [
    path('', index, name='home-page'),
    path('post', post, name='post-page'),
    path('post/<int:pk>', post_detail, name='post-detail-page')
]