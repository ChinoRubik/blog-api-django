from rest_framework.viewsets import ModelViewSet
from categories.api.permissions import IsAdminOrReadOnly
from categories.api.serializers import CategoriesSerializer
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category

class CategoriesViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()
    #queryset = Category.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published']
