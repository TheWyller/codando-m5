from rest_framework import serializers
from categories.serializers import CategorySerializer
from .models import Post
from rest_framework.validators import UniqueValidator
from users.serializers import UserSerializer
from languages.serializers import LanguageSerializer
from commets.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    language = LanguageSerializer(read_only=True)
    categories = CategorySerializer(read_only=True, many=True)
    comments = CommentSerializer(read_only=True, many=True)
    likes = serializers.SerializerMethodField(read_only=True)
    dislikes = serializers.SerializerMethodField(read_only=True)

    def get_likes(self, post: Post):
        return post.likes.count()

    def get_dislikes(self, post: Post):
        return post.dislikes.count()

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
            "likes",
            "dislikes",
        ]
        read_only_fields = ["likes,dislikes"]
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
            },
        }
   

class PostListSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only=True)
    categories = CategorySerializer(read_only=True, many=True)
    likes = serializers.SerializerMethodField(read_only=True)
    dislikes = serializers.SerializerMethodField(read_only=True)

    def get_likes(self, post: Post):
        return post.likes.count()

    def get_dislikes(self, post: Post):
        return post.dislikes.count()

    class Meta:
        model = Post
        fields = [
            "id",
            "language",
            "categories",
            "date",
            "url_doc",
            "is_active",
            "title",
            "description",
            "url_logo",
            "likes",
            "dislikes",
        ]
        read_only_fields = ["likes,dislikes"]
       
