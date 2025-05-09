# Generated by Django 4.2.6 on 2024-01-01 04:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Production', '0002_remove_product_product_code_productionorder'),
        ('Inventory', '0003_rename_quantity_rawmaterialinventory_quantity_on_hand_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_required', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Production.product')),
                ('raw_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.rawmaterial')),
            ],
            options={
                'db_table': 'product_raw_material',
                'unique_together': {('product', 'raw_material')},
            },
        ),
    ]
