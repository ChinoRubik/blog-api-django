from rest_framework.routers import DefaultRouter
from comments.api.views import CommentsViewSets

router_comments = DefaultRouter()

router_comments.register(prefix='comments', basename='comments', viewset=CommentsViewSets)