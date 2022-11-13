from rest_framework.routers import DefaultRouter
from posts.api.views import PostModelViewSet

router_posts_p = DefaultRouter()
router_posts_p.register(prefix='posts', basename='posts', viewset=PostModelViewSet)