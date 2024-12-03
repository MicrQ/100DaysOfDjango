from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    """ view to display all list of posts """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """ used to display details of a single post """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
