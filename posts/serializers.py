from rest_framework import serializers

from categories.serializers import CategorySerializer
from .models import Post
from rest_framework.validators import UniqueValidator
from users.serializers import UserSerializer
from languages.serializers import LanguageSerializer
from .services import get_comments_list, get_interactions_report
from commets.serializers import CommentSerializer
from interactions.serializers import InteractionSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    language = LanguageSerializer(read_only=True)
    categories = CategorySerializer(read_only=True, many=True)
    comments = CommentSerializer(read_only=True, many=True)
    interactions = InteractionSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "language",
            "categories",
            "date",
            "url_doc",
            "is_active",
            "title",
            "description",
            "url_logo",
            "comments",
            "interactions",
        ]
        extra_kwargs = {
            "title": {
                "validators": [
                    UniqueValidator(
                        queryset=Post.objects.all(),
                        message="Post title already exists",
                    )
                ]
            },
            "url_doc": {
                "validators": [
                    UniqueValidator(
                        queryset=Post.objects.all(),
                        message="A post with this documentation link already exists already exists",
                    )
                ]
            }
           
        }

        # comments = serializers.SerializerMethodField(read_only=True)
        # interactions = serializers.SerializerMethodField(read_only=True)

        # def get_comments(self, obj: Post):
        #     return get_comments_list(obj)

        # def get_interactions(self, obj: Post):
        #     return get_interactions_report(obj)
