from .models import Post
from rest_framework import generics
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListAPIView):
    """ view to display all list of posts """
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """ used to display details of a single post """
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
