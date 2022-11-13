from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.api.serializer import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category']
    filterset_fields = ['category__slug']
