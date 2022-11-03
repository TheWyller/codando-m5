from rest_framework import serializers
from commets.models import Comment
from users.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = [
            "id",
            "comment",
            "date_comment",
            "user",
            "post_id"
        ]
        read_only_fields = ["id","post_id"]