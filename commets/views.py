
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from commets.serializers import CommentSerializer
from commets.models import Comment
from users.permissions import CreateListPermission,ListUpdateDeletePermission
class CommentView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CreateListPermission]

    serilizer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ListUpdateDeletePermission]

    lookup_url_kwarg = "comment_id"

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    

    

