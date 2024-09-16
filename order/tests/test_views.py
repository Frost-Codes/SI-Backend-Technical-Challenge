from rest_framework import status

from ..models import Order
from .test_setup import OrderTestSetUp


class OrderDetailsTestView(OrderTestSetUp):
    def test_get_orders_empty(self):
        """
        Test the GET method when the customer has no orders
        :return: None
        """
        response = self.client.get(self.order_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # No orders yet

    def test_get_orders_with_data(self):
        """
        Test the GET method when the customer has made orders
        :return: None
        """
        Order.objects.create(customer=self.customer, item='Test Item', amount=1500)

        response = self.client.get(self.order_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # One order made
        self.assertEqual(response.data[0]['item'], 'Test Item')
        self.assertEqual(response.data[0]['amount'], 1500)

    def test_post_order_with_valid_data(self):
        """
        Test the POST method with valid order data
        :return: None
        """
        self.customer.phone_number = '+254712345678'
        self.customer.save()

        order_data = {
            'item': 'Test Product',
            'amount': 2000,
        }

        response = self.client.post(self.order_url, order_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['item'], 'Test Product')
        self.assertEqual(response.data['amount'], 2000)

    def test_post_order_without_phone_number(self):
        """
        Test the POST method when the user doesn't have a phone number
        :return: None
        """
        self.customer.phone_number = ''
        self.customer.save()

        order_data = {
            'item': 'Test Product',
            'amount': '10',
        }

        response = self.client.post(self.order_url, order_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_order_with_invalid_item_name(self):
        """
        Test the POST method when the user doesn't provide a valid item name
        :return: None
        """
        self.customer.phone_number = '+254712345678'
        self.customer.save()

        order_data = {
            'item': 'T',
            'amount': '10',
        }

        response = self.client.post(self.order_url, order_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_order_with_invalid_amount(self):
        """
        Test the POST method when the user doesn't provide a valid amount
        :return: None
        """
        self.customer.phone_number = '+254712345678'
        self.customer.save()

        order_data = {
            'item': 'Test Product',
            'amount': '0',
        }

        response = self.client.post(self.order_url, order_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



