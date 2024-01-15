from django.test import TestCase
from django.urls import reverse

from Inventory.models import RawMaterial, ProductRawMaterial
from .models import Product


class ProductionViewsTestCase(TestCase):

    def setUp(self):
        # Create some test raw materials
        self.raw_material1 = RawMaterial.objects.create(material_name='RawMaterial1', description='Description1', cost=10.0)
        self.raw_material2 = RawMaterial.objects.create(material_name='RawMaterial2', description='Description2', cost=15.0)

        # Create some test products with associated raw materials
        self.product1 = Product.objects.create(product_name='Product1', description='Description1', unit_price=20.0)
        ProductRawMaterial.objects.create(product=self.product1, raw_material=self.raw_material1, quantity_required=5)

        self.product2 = Product.objects.create(product_name='Product2', description='Description2', unit_price=25.0)
        ProductRawMaterial.objects.create(product=self.product2, raw_material=self.raw_material2, quantity_required=8)

    def test_product_info_view(self):
        # Send a GET request to the product_info_view
        response = self.client.get(reverse('product_info_view'))

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check if products are present in the context
        self.assertIn('products', response.context)

        # Check if the rendered HTML contains the product names, descriptions, unit prices, and raw material details
        self.assertContains(response, 'Product1')
        self.assertContains(response, 'Description1')
        self.assertContains(response, '20.00')  # Check the unit price
        self.assertContains(response, 'RawMaterial1 (5)')  # Check the raw material and quantity

        self.assertContains(response, 'Product2')
        self.assertContains(response, 'Description2')
        self.assertContains(response, '25.00')  # Check the unit price
        self.assertContains(response, 'RawMaterial2 (8)')  # Check the raw material and quantity



