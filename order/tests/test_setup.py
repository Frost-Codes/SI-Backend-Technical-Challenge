from rest_framework.test import APITestCase, APIClient
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

Customer = get_user_model()


class OrderTestSetUp(APITestCase):
    def setUp(self) -> None:
        # test customer
        self.customer = Customer.objects.create_user(
            email='testcustomer@example.com',
            username='test customer',

        )

        # create API client and login customer
        self.client = APIClient()
        self.client.force_authenticate(user=self.customer)

        self.order_url = reverse('order-view')

    def tearDown(self) -> None:
        return super().tearDown()
