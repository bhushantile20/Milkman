from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Customer

class CustomerAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testcustomer', password='123456')
        self.customer_data = {
            'user': self.user.id,
            'phone': '9876543210',
            'address': '123 MG Road, Pune',
            'location': 'Koregaon Park'
        }

    def test_create_customer(self):
        response = self.client.post('/api/customers/', self.customer_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
