from rest_framework.test import APITestCase
from categories.models import Category
from users.models import User
from posts.models import Post
from django.core.exceptions import ValidationError
import json


class CategoriesModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.user_data = {
            "username": "testeteste-11",
            "password": "1234",
            "email": "testeteste-11@testeteste-11.com",
            "first_name": "testeteste-11",
            "last_name": "testeteste-11",
        }

        cls.category_data = {"name": "frontend"}
        cls.missing_keys = {}

    def test_should_be_able_create_a_categorie(self):
        category = Category.objects.create(**self.category_data)

        self.assertEqual(category.name, self.category_data["name"])

    def test_should_not_able_create_a_categorie(self):

        with self.assertRaises(ValidationError):
            Category.objects.create(**self.missing_keys).full_clean()
