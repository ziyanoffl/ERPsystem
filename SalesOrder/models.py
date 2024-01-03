from django.db import models

from CRM.models import Customer
from Production.models import Product


# Create your models here.
class SalesOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    ship_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'sales_order'


class SalesOrderItem(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'sales_order_product'
