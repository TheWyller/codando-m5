from rest_framework import generics
from rest_framework.views import Response, Request
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from languages.models import Language
from posts.permissions import ListUpdateDeletePermission
from .models import Post
from categories.models import Category
from .serializers import PostSerializer, PostListSerializer
from categories.serializers import CategorySerializer
from drf_spectacular.utils import extend_schema
from commets.serializers import ListCommentsSerializer
from django_filters import rest_framework as filters


def get_object_by_id(model, **kwargs):
    object = get_object_or_404(model, **kwargs)

    return object


class PostView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        language_id = self.request.data["language"]
        user = self.request.user
        language = get_object_or_404(Language, pk=language_id)
        categories = []

        categories_data = self.request.data["categories"]
        for item in categories_data:
            item["name"] = item["name"].lower().strip()

        for item in categories_data:
            data, _ = Category.objects.get_or_create(
                defaults={"name": item["name"]},
                **item,
            )
            categories.append(data)

        serializer.save(language=language, user=user, categories=categories)


@extend_schema(methods=["PUT"], exclude=True)
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ListUpdateDeletePermission]

    lookup_url_kwarg = "post_id"

    serializer_class = PostSerializer
    queryset = Post.objects.all()


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

        current_comments = post.comments.all().filter(user=user)
        current_comments = ListCommentsSerializer(current_comments, many=True)

        return Response(
            {
                "dislike": user_dislike,
                "like": user_like,
                "current_user_comments_on_this_post": current_comments.data,
            }
        )


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


class PostFilter(filters.FilterSet):

    keyword = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Post
        fields = [
            "title",
        ]


class ListPostsWithFiltersView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    serializer_class = PostListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilter


class PostOnCategoryView(generics.ListAPIView):

    serializer_class = PostSerializer
    lookup_url_kwarg = "category_name"

    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        category = get_object_or_404(Category, name__icontains=category_name)
        return category.posts.all()


class PostOnLanguageView(generics.ListAPIView):
    lookup_url_kwarg = "language_name"
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        language_name = self.kwargs["language_name"]
        return Post.objects.filter(language__name__icontains=language_name)
