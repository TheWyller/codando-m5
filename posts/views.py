from django.shortcuts import render
from rest_framework import generics

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from posts.permissions import ListUpdateDeletePermission

from .models import Post
from .serializers import PostSerializer


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
