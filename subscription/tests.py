from rest_framework.test import APITestCase
from .models import SubscriptionType

class SubscriptionAPITestCase(APITestCase):
    def setUp(self):
        self.sub_type_data = {
            'name': 'monthly',
            'duration_days': 30,
            'price_multiplier': 1.10
        }

    def test_create_subscription_type(self):
        response = self.client.post('/api/subscriptions/types/', self.sub_type_data)
        self.assertEqual(response.status_code, 201)
