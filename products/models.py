from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    product_code = models.CharField(max_length=10, unique=True)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        # Generate the product code if it doesn't exist
        if not self.product_code:
            last_product = Product.objects.order_by('product_code').last()
            if last_product:
                last_code = int(last_product.product_code[2:])
                new_code = f"{last_product.product_code[:2]}{last_code + 1:02}"
            else:
                new_code = "PD01"
            self.product_code = new_code

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_code} - {self.product_name}"

    class Meta:
        db_table = 'product'


class Inventory(models.Model):
    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    last_updated = models.DateTimeField(auto_now=True)
    warehouse = models.CharField(max_length=100, blank=True)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Inventory Item #{self.pk} - {self.quantity} units in {self.warehouse or 'Unknown Warehouse'}"
