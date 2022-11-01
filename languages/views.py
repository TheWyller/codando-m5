from django.shortcuts import render
from rest_framework import generics

from .models import Language
from .serializers import LanguageSerializer

from rest_framework.authentication import TokenAuthentication
from languages.permissions import LanguagePermission


from rest_framework.permissions import IsAuthenticated


class LanguageView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [LanguagePermission]

    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class LanguageDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, LanguagePermission]

    lookup_url_kwarg = "language_id"

    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
