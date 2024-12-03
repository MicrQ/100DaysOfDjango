from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """ used to serialize the post model to json and viseversa """
    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'body',
            'created_at',
        )
