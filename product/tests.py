from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product
from category.models import Category

class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='cow_milk')
        self.product_data = {
            'name': 'Cow Milk 1L',
            'category': self.category.id,
            'packet_size': 'one_litre',
            'price': '45.00',
            'stock_available': 50
        }

    def test_create_product(self):
        response = self.client.post('/api/products/', self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
