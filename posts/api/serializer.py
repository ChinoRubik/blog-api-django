from rest_framework import serializers
from posts.models import Post
from users.api.serializers import UserSerializer
from categories.api.serializers import CategoriesSerializer

class PostSerializer(serializers.ModelSerializer):
    #user_data = UserSerializer()
    # category = CategoriesSerializer()
    class Meta:
        model = Post
        fields = ['title', 'user', 'content', 'image', 'slug', 'published', 'category', 'created_at']