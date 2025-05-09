# Generated by Django 4.2.6 on 2023-12-31 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Production', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_code',
        ),
        migrations.CreateModel(
            name='ProductionOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order_date', models.DateTimeField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Production.product')),
            ],
            options={
                'db_table': 'production_order',
            },
        ),
    ]
