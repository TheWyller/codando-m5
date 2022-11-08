from rest_framework.test import APITestCase
from categories.models import Category
from users.models import User
from posts.models import Post
from django.core.exceptions import ValidationError
import json

class CategoriesViewTest(APITestCase):
    
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
        cls.category_data2 = {"name": "frontend2"}
        cls.category_dataUpdate = {"name": "frontend3"}
        cls.missing_keys = {}

    def setUp(self) -> None:
        self.user = self.client.post("/api/users/", self.user_data).data
        self.token = self.client.post("/api/login/", self.user_data).data["token"]
        self.category = self.client.post(
            "/api/categories/",
            self.category_data2,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )
    
    def test_should_be_able_to_create_a_category(self):

        response = self.client.post(
            f'/api/categories/',
            self.category_data,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )

        self.assertEqual(response.status_code, 201)

    def test_should_not_be_able_to_create_a_category(self):

        response = self.client.post(
            f'/api/categories/',
            self.category_data,
        )

        self.assertEqual(response.status_code, 401)

    
    def test_should_be_able_to_list_all_category(self):

        response = self.client.get(
            f'/api/categories/',
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )

        self.assertEqual(response.status_code, 200)

    
    def test_should_be_able_to_list_one_category(self):


        response = self.client.get(
            f'/api/categories/{self.category.data["id"]}/',
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )

        self.assertEqual(response.status_code, 200)

    
    def test_should_be_able_to_update_one_category(self):


        response = self.client.patch(
            f'/api/categories/{self.category.data["id"]}/',
            self.category_dataUpdate,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )

        self.assertEqual(response.status_code, 200)

    
    def test_should_be_able_to_delete_one_category(self):


        response = self.client.delete(
            f'/api/categories/{self.category.data["id"]}/',
            self.category_dataUpdate,
            HTTP_AUTHORIZATION=f"Token {self.token}",
        )

        self.assertEqual(response.status_code, 204)

    
