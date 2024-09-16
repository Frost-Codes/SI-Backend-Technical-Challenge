from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse

Customer = get_user_model()


class CustomerTestSetUp(APITestCase):
    def setUp(self) -> None:

        # test customer
        self.customer = Customer.objects.create_user(
            email='testcustomer@example.com',
            username='test customer',

        )

        # create API client and login customer
        # self.client = APIClient()
        self.client.force_authenticate(user=self.customer)

        # urls
        self.customer_details_url = reverse('customer-details')
        self.logout_url = reverse('api-logout')
        self.google_auth_url = reverse('google-auth')

    def tearDown(self) -> None:
        return super().tearDown()


class GoogleOAuth2TestSetUp(APITestCase):
    def setUp(self):
        self.login_url = reverse('social:begin', args=['google-oauth2'])
        self.complete_url = reverse('social:complete', args=['google-oauth2'])

    def tearDown(self) -> None:
        return super().tearDown()



