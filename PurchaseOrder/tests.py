from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from CRM.models import Supplier
from Inventory.models import RawMaterial, Warehouse, RawMaterialInventory
from PurchaseOrder.forms import PurchaseOrderForm
from PurchaseOrder.models import PurchaseOrder


class PurchaseOrderViewsTestCase(TestCase):
    def setUp(self):
        # Create test data for the models
        self.supplier = Supplier.objects.create(name='Test Supplier')
        self.raw_material = RawMaterial.objects.create(material_name='Test Raw Material', description='Test Description', cost=10.0)
        self.warehouse = Warehouse.objects.create(name='Test Warehouse')
        self.purchase_order_data = {
            'supplier': self.supplier,
            'raw_material': self.raw_material,
            'order_date': timezone.now().date(),
            'quantity': 100,
            'total_price': Decimal('500.00'),
            'warehouse': self.warehouse,
        }

    def test_purchase_order_list_view(self):
        # Test rendering purchase order list view
        response = self.client.get(reverse('purchase_order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Purchase Management/view_purchase_orders.html')
