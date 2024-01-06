from django.db import models

from CRM.models import Supplier
from Inventory.models import RawMaterial, Warehouse


# Create your models here.
class PurchaseOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    order_date = models.DateField()
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    class Meta:
        db_table = 'purchase_order'
