from posts.models import Post
from django.test import TestCase
from languages.models import Language
from categories.models import Category
from users.models import User
from django.core.exceptions import ValidationError

class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.user_data = {
            "username": "Wyller",
            "password": "1234",
            "email": "wyller@wyller.com",
            "first_name": "Wyller",
            "last_name": "Fernandes"
        }

        cls.language_data = {
            "name": "language_test"
        }

        cls.category_data = {"name": "frontend"}

        cls.post_data = {
            "url_doc":"teste",
            "title":"teste",
            "description":"e",
            "url_logo":"sss"
        }

        cls.missing_keys = {}

    def test_create_a_post_successfully(self):

        user = User.objects.create(**self.user_data)
        language = Language.objects.create(**self.language_data)
        category = Category.objects.create(**self.category_data)
        post = Post.objects.create(**self.post_data, user=user, language=language)
        post.categories.add(category)

        self.assertEqual(post.url_doc, self.post_data["url_doc"])
        self.assertEqual(post.title, self.post_data["title"])
        self.assertEqual(post.description, self.post_data["description"])
        self.assertEqual(post.url_logo, self.post_data["url_logo"])

    def test_return_error_if_post_is_created_missing_necessary_keys(self):
        
        user = User.objects.create(**self.user_data)
        language = Language.objects.create(**self.language_data)
        category = Category.objects.create(**self.category_data)
        post = Post.objects.create(**self.post_data, user=user, language=language)
        post.categories.add(category)

        with self.assertRaises(ValidationError):
            Post.objects.create(
                **self.missing_keys, user=user, language=language
            ).full_clean()
