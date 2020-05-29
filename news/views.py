from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

from news.models import Post, Comment
from news.serializers import PostSerializer, CommentSerializer


class Pagination(PageNumberPagination):
    """
    Pagination class for API
    """
    page_size = 20
    page_size_query_param = 'page_size'


class PostListApiView(generics.ListCreateAPIView):
    """
    Api for create post or get list of posts.

    GET: /posts/ - for return list of post with pagination and ordering
        For change pagination size use query parameter 'page_size', for change
    page - 'page'.
        For ordering use query parameter 'ordering' with choices: 'id',
    'votes', 'author_name', 'title'.

    POST: /posts/ - for create new post.
        Body params
            "title" -> string(required)
            "link" -> string(required)
            "author_name" -> string(required)
            "votes" -> integer (not required, default = 0)
    """
    serializer_class = PostSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ('id', 'votes', 'author_name', 'title')
    queryset = Post.objects.all()


class PostApiView(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentListApiView(generics.ListCreateAPIView):
    """
    Api for create comment or get list of comments from post

    GET: /posts/<post_id>/comments - for return list of comments with
    pagination and ordering.
        For change pagination size use query parameter 'page_size', for change
    page - 'page'.
        For ordering use query parameter 'ordering' with choices: 'id',
    'author_name'.

    POST: /posts/<post_id>/comments  - for create new comments.
        Body params
            "content" -> string(required)
            "author_name" -> string(required)
    """
    serializer_class = CommentSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ('id', 'author_name')
    queryset = Comment.objects.all()

    def post(self, request, *args, **kwargs):
        request.data['post'] = kwargs['post_id']
        return self.create(request, *args, **kwargs)


class CommentApiView(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
