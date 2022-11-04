from rest_framework import generics
from rest_framework.views import Response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from languages.models import Language
from posts.permissions import ListUpdateDeletePermission,HasPostPermission
from .models import Post
from categories.models import Category
from .serializers import PostSerializer, PostListSerializer
from categories.serializers import CategorySerializer
from drf_spectacular.utils import extend_schema


def get_object_by_id(model, **kwargs):
    object = get_object_or_404(model, **kwargs)

    return object


class PostView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        language_id = self.request.data["language"]
        user = self.request.user
        language = get_object_or_404(Language, pk=language_id)
        categories = []
        categories_data = self.request.data["categories"]
        for item in categories_data:
            categories.append(get_object_or_404(Category, id=item))

        serializer.save(language=language, user=user, categories=categories)


@extend_schema(methods=["PUT"], exclude=True)
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ListUpdateDeletePermission]

    lookup_url_kwarg = "post_id"

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostOnCategoryView(generics.ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_url_kwarg = "category_id"

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        category = get_object_by_id(Category, id=category_id)
        return category.posts


class PostOnLanguageView(generics.ListAPIView):
    lookup_url_kwarg = "language_id"

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        language_id = self.kwargs["language_id"]

        return Post.objects.filter(language=language_id)


class PostsSelfUser(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user

        return Post.objects.filter(user=user.id)


class AddLike(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user

        post_id = kwargs["post_id"]
        post = get_object_or_404(Post, id=post_id)

        dislikes_array = post.dislikes.all()
        if user in dislikes_array:
            post.dislikes.remove(user)

        likes_array = post.likes.all()
        if user in likes_array:
            post.likes.remove(user)
            return Response({"dislike": False, "like": False})
        post.likes.add(user)
        return Response({"dislike": False, "like": True})


class AddDislike(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        
        post_id = kwargs["post_id"]
        post = get_object_or_404(Post, id=post_id)
        likes_array = post.likes.all()
        if user in likes_array:
            post.likes.remove(user)

        dislikes_array = post.dislikes.all()
        if user in dislikes_array:
            post.dislikes.remove(user)
            return Response({"dislike": False, "like": False})
        post.dislikes.add(user)
        return Response({"dislike": True, "like": False})


class ListPostUserRelationInteraction(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        post_id = kwargs["post_id"]
        post = get_object_or_404(Post, id=post_id)

        user_dislike = False
        user_like = False

        dislikes_array = post.dislikes.all()
        likes_array = post.likes.all()

        if user in dislikes_array:
            user_dislike = True
        if user in likes_array:
            user_like = True

        return Response({"dislike": user_dislike, "like": user_like})

class ListAllDislikesInteractions(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostListSerializer

    def get_queryset(self):
        return self.request.user.dislikes.all()
   
    

class ListAllLikesInteractions(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostListSerializer

    def get_queryset(self):
       return self.request.user.likes.all()