from django.shortcuts import render
from rest_framework import generics

from .models import Category
from .serializers import CategorySerializer

from rest_framework.authentication import TokenAuthentication
from categories.permissions import CategoryPermission

from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema


class CategoryView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CategoryPermission]

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

@extend_schema(methods=['PUT'], exclude=True)
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, CategoryPermission]

    lookup_url_kwarg = "category_id"

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
