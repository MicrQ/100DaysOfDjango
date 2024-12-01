from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """ model to json serializer """
    class Meta:
        model = Todo
        fields = ('id', 'title', 'body')
