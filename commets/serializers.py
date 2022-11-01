from rest_framework import serializers
from commets.models import Comment

class CommentSerializer(serializers.Modelserializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "comment",
            "date_comment",
            "user_id",
            "post_id"
        ]
        read_only_fields = ["id","user_id","post_id"]