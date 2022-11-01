from django.shortcuts import render
from rest_framework import generics

from django.shortcuts import get_object_or_404

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from posts.permissions import ListUpdateDeletePermission

from .models import Post
from categories.models import Category

from .serializers import PostSerializer
from categories.serializers import CategorySerializer


def get_object_by_id(model, **kwargs):
    object = get_object_or_404(model, **kwargs)

    return object


class PostView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = PostSerializer
    queryset = Post.objects.all()


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
