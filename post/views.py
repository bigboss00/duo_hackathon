from django_filters import rest_framework as rest_filter
from rest_framework import viewsets, filters, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Post, Comment
from .serializers import PostListSerializer, PostDetailSerializer, CreatePostSerializer, CommentSerializer
from .permissions import IsAuthorOrIsAdmin, IsCommentAuthor


class PostFilter(rest_filter.FilterSet):
    created = rest_filter.DateTimeFromToRangeFilter()

    class Meta:
        model = Post
        fields = ('status', 'created')


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthorOrIsAdmin, ]
    filter_backends = [rest_filter.DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    filterset_class = PostFilter
    search_fields = ['title', 'body']
    ordering_fields = ['created_at', 'title']

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'retrieve':
            return PostDetailSerializer
        return CreatePostSerializer


class CommentsViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permission(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsCommentAuthor()]

