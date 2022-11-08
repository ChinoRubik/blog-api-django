from rest_framework.routers import DefaultRouter
from categories.api.views import CategoriesViewSet

router_post = DefaultRouter()
router_post.register(prefix = 'category', basename = 'category', viewset = CategoriesViewSet)