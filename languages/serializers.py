from rest_framework import serializers
from .models import Language
from rest_framework.validators import UniqueValidator


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = [
            "id",
            "name",
            "url_doc",
        ]
        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Language.objects.all(),
                        message="language name already exists",
                    )
                ]
            },
            "url_doc": {
                "validators": [
                    UniqueValidator(
                        queryset=Language.objects.all(),
                        message="documentation link already exists already exists",
                    )
                ]
            },
        }
