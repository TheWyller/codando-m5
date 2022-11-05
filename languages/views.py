from django.shortcuts import render
from rest_framework import generics

from .models import Language
from .serializers import LanguageSerializer

from rest_framework.authentication import TokenAuthentication
from languages.permissions import LanguagePermission


from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema


class LanguageView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [LanguagePermission]

    serializer_class = LanguageSerializer
    queryset = Language.objects.all()

@extend_schema(methods=['PUT'], exclude=True)
class LanguageDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, LanguagePermission]

    lookup_url_kwarg = "language_id"

    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
