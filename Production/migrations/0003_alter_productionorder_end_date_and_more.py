# Generated by Django 4.2.6 on 2024-01-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Production', '0002_remove_product_product_code_productionorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionorder',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='productionorder',
            name='order_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='productionorder',
            name='start_date',
            field=models.DateField(),
        ),
    ]
