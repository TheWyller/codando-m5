from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from commets.serializers import CommentSerializer
from commets.models import Comment
from posts.models import Post
from .permissions import ListUpdateDeletePermission
from drf_spectacular.utils import extend_schema


class CommentView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs["post_id"]
        post = get_object_or_404(Post, pk=post_id)

        serializer.save(user_id=user.id, post_id=post.id)


@extend_schema(methods=['PUT'], exclude=True)
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ListUpdateDeletePermission]

    lookup_url_kwarg = "comment_id"

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
