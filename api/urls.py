from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register('follow', FollowViewSet)
router.register('group', GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
