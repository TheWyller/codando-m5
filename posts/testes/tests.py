from rest_framework.test import APITestCase
from categories.models import Category
from languages.models import Language
from users.models import User
from posts.models import Post
from commets.models import Comment
from django.core.exceptions import ValidationError
import json


class CommentModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_data = {
            "username": "testeteste-11",
            "password": "1234",
            "email": "testeteste-11@testeteste-11.com",
            "first_name": "testeteste-11",
            "last_name": "testeteste-11",
        }
        cls.language_data = {
            "name": "python",
        }
        cls.category_data = {"name": "frontend"}
        cls.post_data = {
            "url_doc": "teste1",
            "title": "teste2",
            "description": "desc",
            "url_logo": "https://teste",
        }
        cls.missing_keys = {}

    def test_should_be_able_create_a_post(self):
        """
        it should be able to create a post
        """
        user = User.objects.create(**self.user_data)
        language = Language.objects.create(**self.language_data)
        category = Category.objects.create(**self.category_data)
        post = Post.objects.create(
            **self.post_data, user=user, language=language
            )
        post.categories.add(category)

        self.assertEqual(post.title, self.post_data["title"])
        self.assertEqual(post.user.username, self.user_data["username"])
        self.assertEqual(post.user.email, self.user_data["email"])
        self.assertEqual(post.language.name, self.language_data["name"])

    def test_should_not_be_able_to_create_a_post(self):
        """
        it should not be able to create a post with missing keys input
        """
        user = User.objects.create(**self.user_data)
        language = Language.objects.create(**self.language_data)
        with self.assertRaises(ValidationError):
            Post.objects.create(
                **self.missing_keys, user=user, language=language
            ).full_clean()


class CommentViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_data = {
            "username": "testeteste-11",
            "password": "1234",
            "email": "testeteste-11@testeteste-11.com",
            "first_name": "testeteste-11",
            "last_name": "testeteste-11",
        }
        cls.language_data = {
            "name": "python",
        }
        cls.category_data = {"name": "frontend"}
        cls.post_data = {
            "language": "",
            "categories": [{"name": "react"}, {"name": "backend"}],
            "url_doc": "teste1",
            "title": "teste2",
            "description": "desc",
            "url_logo": "https://teste",
        }
        cls.missing_keys = {}
        cls.user = {}
        cls.token = {}
        cls.language = {}
        cls.post_obj = {}

    def setUp(self) -> None:
        self.user = self.client.post("/api/users/", self.user_data).data
        self.token = self.client.post(
            "/api/login/",
            self.user_data
            ).data["token"]
        self.language = self.client.post(
            "/api/languages/",
            self.language_data,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        ).data
        self.post_data["language"] = self.language["id"]

    def test_should_be_able_to_create_a_post(self):
        """
        it should be able to create a post
        """
        response = self.client.post(
            f'/api/posts/',
            json.dumps(self.post_data),
            HTTP_AUTHORIZATION=f"Token {self.token}",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], self.post_data["title"])
        self.assertEqual(
            response.data["user"]["username"],
            self.user_data["username"]
            )
        self.assertEqual(
            response.data["user"]["email"],
            self.user_data["email"]
            )
        self.assertEqual(
            response.data["language"]["name"],
            self.language_data["name"]
            )

    def test_should_not_be_able_to_create_a_post(self):
        """
        it should not be able to create a post with missing keys input
        """
        response = self.client.post(
            f'/api/posts/',
            self.missing_keys,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )
        self.assertEqual(response.status_code, 400)
        print(response.data)
        self.assertEqual(
              response.data["title"][0],
              "This field is required.")
        self.assertEqual(
              response.data["url_doc"][0],
              "This field is required.")
        self.assertEqual(
              response.data["description"][0],
              "This field is required.")
        self.assertEqual(
              response.data["url_logo"][0],
              "This field is required.")
