from rest_framework.viewsets import ModelViewSet
from categories.api.permissions import IsAdminOrReadOnly
from categories.api.serializers import CategoriesSerializer
from categories.models import Category

class CategoriesViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()
