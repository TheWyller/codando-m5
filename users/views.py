from django.shortcuts import render
from rest_framework import generics
from .models import User

from .serializers import UserSerializer, UserUpdatedSerializer
from rest_framework.authentication import TokenAuthentication
from users.permissions import CreateListPermission, ListUpdateDeletePermission
from rest_framework.permissions import IsAdminUser
from drf_spectacular.utils import extend_schema


class UserView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CreateListPermission]

    serializer_class = UserSerializer
    queryset = User.objects.all()

@extend_schema(methods=['PUT'], exclude=True)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ListUpdateDeletePermission]

    lookup_url_kwarg = "user_id"

    serializer_class = UserUpdatedSerializer
    queryset = User.objects.all()
