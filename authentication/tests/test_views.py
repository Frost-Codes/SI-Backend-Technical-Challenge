from rest_framework import status
from unittest.mock import patch  # used to fake specific functions or objects during the test
import requests_mock  # allows mocking of http requests like those made by requests library

from .test_setup import CustomerTestSetUp, GoogleOAuth2TestSetUp
from ..models import Customer


class TestCustomerView(CustomerTestSetUp):

    def test_customer_logout(self):
        """
        Test that a logged in customer can log out
        :return: None
        """
        response = self.client.post(self.logout_url)

        # asserts logout
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        self.assertEqual(response.data['detail'], 'Successfully logged out.')

    def test_get_customer_details(self):
        """
        Test that an authenticated user can retrieve their customer details via GET request
        :return: None
        """

        response = self.client.get(self.customer_details_url)

        # check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # check returned data matches user details
        self.assertEqual(response.data['email'], self.customer.email)
        self.assertEqual(response.data['username'], self.customer.username)

    def test_update_customer_phone_number(self):
        """
        Test that an authenticated user can update their phone number via PUT request
        :return: None
        """

        updated_data = {
            'phone_number': '+254727832711'
        }

        response = self.client.put(self.customer_details_url, data=updated_data)

        # check status code is 202 accepted

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        # check phone number is updated correctly
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.phone_number, updated_data['phone_number'])
        self.assertEqual(response.data['phone_number'], updated_data['phone_number'])

    def test_put_invalid_phone_number(self):
        """
        Test customer phone number field cannot be updated with an invalid phone number
        :return: None
        """

        invalid_data = ['+25477322018', '+2547227322018', '+255727322018', '+255027322018']

        for number in invalid_data:

            response = self.client.put(self.customer_details_url, data={'phone_number': number})

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GoogleOAuth2TestCase(GoogleOAuth2TestSetUp):

    @requests_mock.Mocker()
    @patch('social_core.backends.google.GoogleOAuth2.user_data')
    def test_google_oauth2_login(self, mock_requests, mock_user_data):
        """
        Test Google OAuth2 login flow
        """
        # Mock Google's token endpoint response
        mock_requests.post('https://oauth2.googleapis.com/token', json={
            'access_token': 'ya29.a0AfH6SMBQZ',
            'expires_in': 3599,
            'token_type': 'Bearer',
            'refresh_token': '1//03rAvR',
            'id_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjUzOTAxZjczM',
        })

        # Mock Google's customer info API response
        mock_user_data.return_value = {
            'id': '123456789',
            'email': 'testuser@gmail.com',
            'verified_email': True,
            'name': 'Test User',
            'given_name': 'Test',
            'family_name': 'User',
        }

        # simulate user visiting login page for Google OAuth2
        # sends get request to auth/login/google-oauth2
        # will redirect to accounts.google.com with client_id
        response = self.client.get(self.login_url)

        # make sure redirect to google's OAuth2 endpoint
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertIn('https://accounts.google.com/o/oauth2/auth', response.url)

        # Mock Google's redirect back to the app with authorization code
        mock_requests.post('https://accounts.google.com/o/oauth2/token', json={
            'access_token': 'test_access_token',
            'token_type': 'Bearer',
            'expires_in': 3600,
            'refresh_token': 'test_refresh_token',
        })

        # Simulate Google's redirect back to your app
        response = self.client.get(f'{self.complete_url}?code=4/0AY0e-g52H9&state={response.url.split("state=")[1]}')

        # Check redirect back to home
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertRedirects(response, '/')

        # Check if the customer was created in the database
        customer = Customer.objects.get(email='testuser@gmail.com')
        self.assertIsNotNone(customer)
        self.assertEqual(customer.email, 'testuser@gmail.com')
        self.assertEqual(customer.first_name, 'Test')
        self.assertEqual(customer.last_name, 'User')
