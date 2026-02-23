# from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class UsersAPITestCase(APITestCase):
    def setUp(self):
        self.milkman = User.objects.create_user(
            username='milkman', 
            email='milkman@example.com', 
            password='123456',
            is_staff=True
        )

    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
