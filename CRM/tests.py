from django.test import TestCase
from django.urls import reverse

from CRM.models import Customer, Supplier


class CRMViewsTestCase(TestCase):
    def test_customer_management_view(self):
        # Test rendering customer management view
        response = self.client.get(reverse('customer_management_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CRM/view_customer.html')

        # Test submitting a valid form
        data = {
            'name': 'Test Customer',
            'phone': '1234567890',
            'email': 'test@example.com',
            'address': 'Test Address'
        }
        response = self.client.post(reverse('customer_management_view'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission

        # Check if a new customer is created
        self.assertTrue(Customer.objects.filter(name='Test Customer', email='test@example.com').exists())

    def test_customer_update_view(self):
        # Create a test customer
        customer = Customer.objects.create(name='Test Customer', email='test@example.com')

        # Test rendering customer update view
        response = self.client.get(reverse('customer_update', args=[customer.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CRM/update_customer.html')

        # Test submitting a valid form
        data = {
            'name': 'Updated Customer',
            'phone': '9876543210',
            'email': 'updated@example.com',
            'address': 'Updated Address'
        }
        response = self.client.post(reverse('customer_update', args=[customer.pk]), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission

        # Check if the customer is updated
        customer.refresh_from_db()
        self.assertEqual(customer.name, 'Updated Customer')
        self.assertEqual(customer.email, 'updated@example.com')

    def test_supplier_management_view(self):
        # Test rendering supplier management view
        response = self.client.get(reverse('supplier_management_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CRM/view_supplier.html')

        # Test submitting a valid form
        data = {
            'name': 'Test Supplier',
            'phone': '1234567890',
            'email': 'supplier@example.com',
            'address': 'Test Address'
        }
        response = self.client.post(reverse('supplier_management_view'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission

        # Check if a new supplier is created
        self.assertTrue(Supplier.objects.filter(name='Test Supplier', email='supplier@example.com').exists())

    def test_supplier_update_view(self):
        # Create a test supplier
        supplier = Supplier.objects.create(name='Test Supplier', email='supplier@example.com')

        # Test rendering supplier update view
        response = self.client.get(reverse('supplier_update', args=[supplier.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CRM/update_supplier.html')

        # Test submitting a valid form
        data = {
            'name': 'Updated Supplier',
            'phone': '9876543210',
            'email': 'updated_supplier@example.com',
            'address': 'Updated Address'
        }
        response = self.client.post(reverse('supplier_update', args=[supplier.pk]), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission

        # Check if the supplier is updated
        supplier.refresh_from_db()
        self.assertEqual(supplier.name, 'Updated Supplier')
        self.assertEqual(supplier.email, 'updated_supplier@example.com')
