from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class ERPViewsTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Common setup for all test cases
        cls.login_url = reverse('login_view')
        cls.custom_login_url = reverse('custom_login')

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='admin', password='admin')

    def test_login_view(self):
        # Test the login view
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200, msg="Login view should return a successful response.")

    def test_custom_login_successful(self):
        # Test the custom login view with valid credentials
        response = self.client.post(self.custom_login_url, {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 302, msg="Successful login should redirect.")
        self.assertRedirects(response, reverse('home_view'), msg_prefix="Redirect should go to home_view.")

    # def test_custom_login_unsuccessful(self):
    #     # Test the custom login view with invalid credentials
    #     response = self.client.post(self.custom_login_url, {'username': 'admin', 'password': 'wrongpassword'})
    #     self.assertEqual(response.status_code, 200, msg="Unsuccessful login should stay on the login page.")
    #     self.assertContains(response, 'Invalid login credentials.', msg_prefix="Error message should be present.")
