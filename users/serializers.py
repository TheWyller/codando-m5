from attr import field
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = [
            "id", "username", "email", "password", "first_name",
            "last_name", "is_superuser", "is_active", "date_joined"]

        read_only_fields = ["is_superuser", "is_active", "date_joined"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
