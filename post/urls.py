from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostsViewSet, CommentsViewSet

router = SimpleRouter()
router.register('posts', PostsViewSet, 'posts')
router.register('comments', CommentsViewSet, 'comments')

urlpatterns = [
    path('', include(router.urls))
]
