from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# Import the Product model
from Production.models import Product
from .forms import WarehouseForm, RawMaterialForm
from .models import Warehouse, RawMaterial, ProductInventory


class InventoryViewsTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='admin', password='admin')

        # Create test data for models
        self.warehouse = Warehouse.objects.create(name='Test Warehouse', location='Test Location')
        self.raw_material = RawMaterial.objects.create(material_name='Test Material', description='Test Description',
                                                       cost=10.0)

        # Create a Product instance for the ProductInventory model
        self.product = Product.objects.create(product_name='Test Product', description='Test Product Description',
                                              unit_price=15.0)

        # Use the Product instance when creating the ProductInventory instance
        self.product_inventory = ProductInventory.objects.create(product=self.product, warehouse=self.warehouse,
                                                                 quantity_on_hand=50)

    def test_warehouse_management_view(self):
        # Ensure the view returns a 200 status code
        response = self.client.get(reverse('warehouse_management_view'))
        self.assertEqual(response.status_code, 200)

        # Ensure the form is rendered
        self.assertContains(response, '<form')
        self.assertIsInstance(response.context['form'], WarehouseForm)

    def test_warehouse_update(self):
        # Ensure the view returns a 200 status code
        response = self.client.get(reverse('warehouse_update', args=[self.warehouse.pk]))
        self.assertEqual(response.status_code, 200)

        # Ensure the form is rendered
        self.assertContains(response, '<form')
        self.assertIsInstance(response.context['form'], WarehouseForm)

    def test_warehouse_delete(self):
        # Ensure the view returns a 200 status code
        response = self.client.get(reverse('warehouse_delete', args=[self.warehouse.pk]))
        self.assertEqual(response.status_code, 200)

        # Ensure the confirmation form is rendered
        self.assertContains(response, '<form')

    def test_raw_material_view(self):
        # Ensure the view returns a 200 status code
        response = self.client.get(reverse('raw_material_view'))
        self.assertEqual(response.status_code, 200)

        # Ensure the form is rendered
        self.assertContains(response, '<form')
        self.assertIsInstance(response.context['form'], RawMaterialForm)

    def test_raw_material_update(self):
        # Ensure the view returns a 200 status code
        response = self.client.get(reverse('raw_material_update', args=[self.raw_material.pk]))
        self.assertEqual(response.status_code, 200)

        # Ensure the form is rendered
        self.assertContains(response, '<form')
        self.assertIsInstance(response.context['form'], RawMaterialForm)

    def test_create_product(self):
        # Ensure the view returns a 200 status code
        response = self.client.get(reverse('create_product'))
        self.assertEqual(response.status_code, 200)

        # Ensure the form is not in the context
        self.assertNotIn('form', response.context)

    def test_product_inventory_view(self):
        # Ensure the view returns a 200 status code
        response = self.client.get(reverse('product_inventory'))
        self.assertEqual(response.status_code, 200)

        # Ensure the expected content is in the response
        self.assertContains(response, 'Test Product')

    # Add more test cases as needed
