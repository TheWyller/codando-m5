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
        cls.comment_data = {"comment": "post legal"}
        cls.missing_keys = {}

    def test_should_be_able_create_a_comment(self):
        """
        it should be able to create a comment
        """
        user = User.objects.create(**self.user_data)
        language = Language.objects.create(**self.language_data)
        category = Category.objects.create(**self.category_data)
        post = Post.objects.create(**self.post_data, user=user, language=language)
        post.categories.add(category)
        comment = Comment.objects.create(**self.comment_data, user=user, post=post)
        self.assertEqual(comment.comment, self.comment_data["comment"])
        self.assertEqual(comment.user.username, self.user_data["username"])
        self.assertEqual(comment.user.email, self.user_data["email"])

    def test_should_not_be_able_to_create_a_comment(self):
        """
        it should not be able to create a comment with missing keys input
        """
        user = User.objects.create(**self.user_data)
        language = Language.objects.create(**self.language_data)
        category = Category.objects.create(**self.category_data)
        post = Post.objects.create(**self.post_data, user=user, language=language)
        post.categories.add(category)
        with self.assertRaises(ValidationError):
            Comment.objects.create(
                **self.missing_keys, user=user, post=post
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
        cls.comment_data = {"comment": "post legal"}
        cls.missing_keys = {}
        cls.user = {}
        cls.token = {}
        cls.language = {}
        cls.post_obj = {}

    def setUp(self) -> None:
        self.user = self.client.post("/api/users/", self.user_data).data
        self.token = self.client.post("/api/login/", self.user_data).data["token"]
        self.language = self.client.post(
            "/api/languages/",
            self.language_data,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        ).data
        self.post_data["language"] = self.language["id"]

        self.post_obj = self.client.post(
            "/api/posts/",
            json.dumps(self.post_data),
            HTTP_AUTHORIZATION=f"Token {self.token}",
            content_type="application/json",
        ).data

    def test_should_be_able_to_create_a_comment(self):
        """
        it should be able to create a comment
        """
        response = self.client.post(
            f'/api/posts/{self.post_obj["id"]}/comments/',
            self.comment_data,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["comment"], self.comment_data["comment"])
        self.assertEqual(response.data["user"]["username"], self.user_data["username"])
        self.assertEqual(response.data["user"]["email"], self.user_data["email"])

    def test_should_not_be_able_to_create_a_comment(self):
        """
        it should not be able to create a comment with missing keys input
        """
        response = self.client.post(
            f'/api/posts/{self.post_obj["id"]}/comments/',
            self.missing_keys,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["comment"][0], "This field is required.")
