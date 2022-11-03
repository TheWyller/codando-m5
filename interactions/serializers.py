from rest_framework import serializers
from .models import Interaction, InteractionType


class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = [
            "id",
            "user",
            "post",
            "date_interaction",
            "interaction",
        ]
        extra_kwargs = {
            "user": {"read_only": True},
            "post": {"read_only": True},
        }
