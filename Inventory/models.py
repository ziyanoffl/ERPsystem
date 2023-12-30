from django.core.validators import MinValueValidator
from django.db import models

from Production.models import Product


# Create your models here.
class RawMaterial(models.Model):
    raw_material_id = models.AutoField(primary_key=True)
    material_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'raw_material'


class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    class Meta:
        db_table = 'warehouse'


class RawMaterialInventory(models.Model):
    raw_material_id = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    last_updated = models.DateTimeField(auto_now=True)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    class Meta:
        db_table = 'raw_material_inventory'
