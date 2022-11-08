from rest_framework.test import APITestCase
from posts.models import Post
from posts.serializers import PostSerializer, PostListSerializer
from rest_framework.views import status
from languages.models import Language
from categories.models import Category
from users.models import User
from rest_framework.authtoken.models import Token
import json


class PostViewsTest(APITestCase):

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

        cls.post_data = {
            "language": "",
            "categories": [{"name": "frontend"}],
            "url_doc":"teste",
            "title":"teste",
            "description":"e",
            "url_logo":"sss"
        }

    def setUp(self):

        self.user = self.client.post("/api/users/", self.user_data).data
        
        self.token = self.client.post("/api/login/", self.user_data).data["token"]
        
        self.language = self.client.post(
            "/api/languages/",
            self.language_data,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        ).data
        
        self.post_data["language"] = self.language["id"]

    def test_can_create_post(self):

        # self.post_data.categories.set(self.category)

        response = self.client.post(
            "/api/posts/", 
            json.dumps(self.post_data),
            HTTP_AUTHORIZATION=f"Token {self.token}",
            content_type="application/json",
        )

        expect_status_code = status.HTTP_201_CREATED
        result_status_code = response.status_code

        self.assertEqual(expect_status_code, result_status_code)

    def test_return_an_error_when_creating_a_post_with_title_and_url_doc_already_existing(self):

        # self.post_data.categories.set(self.category)

        self.client.post(
            "/api/posts/", 
            json.dumps(self.post_data),
            HTTP_AUTHORIZATION=f"Token {self.token}",
            content_type="application/json",
        )

        response = self.client.post(
            "/api/posts/", 
            json.dumps(self.post_data),
            HTTP_AUTHORIZATION=f"Token {self.token}",
            content_type="application/json",
        )

        expect_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code

        self.assertEqual(expect_status_code, result_status_code)

    def test_can_list_all_posts(self):

        self.client.post(
            "/api/posts/", 
            json.dumps(self.post_data),
            HTTP_AUTHORIZATION=f"Token {self.token}",
            content_type="application/json",
        )

        response = self.client.get("/api/posts/", HTTP_AUTHORIZATION=f"Token {self.token}")

        expect_status_code = status.HTTP_200_OK
        self.assertEqual(response.status_code, expect_status_code)

        # self.assertEqual(len(self.posts), len(response.data))

        # for post in self.posts:

        #    self.assertIn(
        #        PostListSerializer(instance=post).data,
        #        response.data
        #   )

    def test_successfully_delete_a_post(self):
        
        post = self.client.post(
            "/api/posts/", 
            json.dumps(self.post_data),
            HTTP_AUTHORIZATION=f"Token {self.token}",
            content_type="application/json",
        ).data
        
        response = self.client.delete(f'/api/posts/{post["id"]}/', HTTP_AUTHORIZATION=f"Token {self.token}")
        
        expect_status_code = status.HTTP_204_NO_CONTENT
        self.assertEqual(response.status_code, expect_status_code)

    def test_list_posts_by_keyword_successfully(self):
        
        post = self.client.post(
            "/api/posts/", 
            json.dumps(self.post_data),
            HTTP_AUTHORIZATION=f"Token {self.token}",
            content_type="application/json",
        ).data
        
        response = self.client.get(f'/api/posts/filter/?keyword={post["title"]}', HTTP_AUTHORIZATION=f"Token {self.token}")
        
        expect_status_code = status.HTTP_200_OK
        self.assertEqual(response.status_code, expect_status_code)

    def test_can_retrieve_a_specific_post(self):
        
        post = self.client.post(
            "/api/posts/", 
            json.dumps(self.post_data),
            HTTP_AUTHORIZATION=f"Token {self.token}",
            content_type="application/json",
        ).data
        
        response = self.client.get(f'/api/posts/{post["id"]}/', HTTP_AUTHORIZATION=f"Token {self.token}")
        
        expect_status_code = status.HTTP_200_OK
        self.assertEqual(response.status_code, expect_status_code)
        self.assertEqual(response.json()['id'], post["id"])
