from django.core.validators import MinValueValidator
from django.db import models

from Production.models import Product


# Create your models here.
class RawMaterial(models.Model):
    raw_material_id = models.AutoField(primary_key=True)
    material_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.material_name}"

    class Meta:
        db_table = 'raw_material'


class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'warehouse'


class RawMaterialInventory(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity_on_hand = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    last_updated = models.DateField(auto_now=True)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    def __str__(self):
        return self.raw_material.material_name

    class Meta:
        db_table = 'raw_material_inventory'


class ProductRawMaterial(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_required = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('product', 'raw_material')
        db_table = 'product_raw_material'


class ProductInventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity_on_hand = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name
    class Meta:
        db_table = 'product_inventory'
