from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from SalesOrder.models import SalesOrder, Customer


class SalesOrderViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='admin', password='admin'
        )

        # Create some test customers
        customer1 = Customer.objects.create(
            name='Customer1', email='customer1@example.com'
        )

        customer2 = Customer.objects.create(
            name='Customer2', email='customer2@example.com'
        )

        # Create some test sales orders
        SalesOrder.objects.create(
            customer=customer1,
            order_date='2024-01-15',
            ship_date='2024-01-20',
            status='Pending',
            total_price=100.00,
        )

        SalesOrder.objects.create(
            customer=customer2,
            order_date='2024-01-16',
            ship_date='2024-01-21',
            status='Shipped',
            total_price=150.00,
        )

    def test_sales_order_view(self):
        # Log in the test user
        self.client.login(username='admin', password='admin')

        # Send GET request to the sales order view
        response = self.client.get(reverse('sales_order'))

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check if the 'sales_orders' context variable contains the expected SalesOrder instances
        expected_output = [
            'SalesOrder object (1)',
            'SalesOrder object (2)',
        ]

        actual_output = list(map(str, response.context['sales_orders']))

        self.assertListEqual(actual_output, expected_output)
