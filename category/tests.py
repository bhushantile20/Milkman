from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Category

class CategoryAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.category_data = {
            'name': 'cow_milk',
            'description': 'Pure A2 cow milk'
        }

    def test_create_category(self):
        response = self.client.post('/api/categories/', self.category_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)

    def test_list_categories(self):
        Category.objects.create(name='buffalo_milk')
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
