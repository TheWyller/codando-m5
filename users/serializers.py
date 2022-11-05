from attr import field
from rest_framework import serializers

from users.models import User
from rest_framework.validators import UniqueValidator


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


class UserUpdatedSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = [
            "id", "username", "email", "password", "first_name",
            "last_name", "is_superuser", "is_active", "date_joined"]

        read_only_fields = ["is_superuser", "date_joined"]
        extra_kwargs = {
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="email already exists",
                    )
                ]
            },
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="username already exists",
                    )
                ]
            }
        }
