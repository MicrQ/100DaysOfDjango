from .models import Todo
from rest_framework import generics
from .serializers import TodoSerializer


class ListTodo(generics.ListAPIView):
    """ used to list all todos """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):
    """ used to retrieve a single todo """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
