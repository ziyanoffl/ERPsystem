from datetime import timedelta

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View

from Inventory.models import ProductRawMaterial, RawMaterial, ProductInventory, RawMaterialInventory, Warehouse
from .models import Product, ProductionOrder


# Create your views here.
def product_info_view(request):
    products = Product.objects.all()

    for product in products:
        product.raw_materials = ProductRawMaterial.objects.filter(product=product)

    return render(request, 'production/product_information.html', {'products': products})


def create_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        unit_price = request.POST.get('unit_price')
        quantity_in_stock = request.POST.get('quantity_in_stock')

        # Create Product
        product = Product.objects.create(
            product_name=product_name,
            description=description,
            unit_price=unit_price,
            quantity_in_stock=quantity_in_stock
        )

        # Process raw materials
        raw_materials = request.POST.getlist('raw_material')
        quantities = request.POST.getlist('quantity_required')

        for raw_material_id, quantity in zip(raw_materials, quantities):
            raw_material = RawMaterial.objects.get(pk=raw_material_id)
            ProductRawMaterial.objects.create(
                product=product,
                raw_material=raw_material,
                quantity_required=quantity
            )

        return redirect('product_info_view')  # Change 'product_list' to your actual product list URL

    raw_materials = RawMaterial.objects.all()
    return render(request, 'production/add_product.html', {'raw_materials': raw_materials})


class CreateProductionOrderView(View):
    template_name = 'production/production_order_form.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        warehouses = Warehouse.objects.all()
        return render(request, self.template_name, {'products': products, 'warehouses': warehouses})

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        warehouse_id = int(request.POST.get('warehouse'))

        print("product_id:", product_id)
        print("quantity:", quantity)
        print("warehouse_id:", warehouse_id)

        # Check if there are enough raw materials
        if not self.has_enough_raw_materials(product_id, quantity, warehouse_id):
            return JsonResponse({'success': False, 'message': 'Not enough raw materials. Production order canceled.'})

        with transaction.atomic():
            # Create a new production order
            production_order = ProductionOrder.objects.create(
                product_id=product_id,
                quantity=quantity,
                order_date=timezone.now(),
                start_date=timezone.now(),
                end_date=timezone.now() + timedelta(days=7),  # Adjust as needed
            )

            # Update ProductInventory
            product = Product.objects.get(pk=product_id)

            # Check if there's already an inventory entry for the product in the specified warehouse
            try:
                product_inventory = ProductInventory.objects.get(product=product, warehouse_id=warehouse_id)
                # Now update the quantity
                product_inventory.quantity_on_hand += quantity
                product_inventory.save()
            except ProductInventory.DoesNotExist:
                # If no inventory entry exists for the product in the specified warehouse, create one
                product_inventory = ProductInventory.objects.create(product=product, warehouse_id=warehouse_id,
                                                                    quantity_on_hand=0)
                product_inventory.quantity_on_hand += quantity
                product_inventory.save()



            # Reduce RawMaterialInventory
            raw_materials = ProductRawMaterial.objects.filter(product=product)
            for raw_material in raw_materials:
                try:
                    raw_material_inventory = RawMaterialInventory.objects.get(
                        raw_material=raw_material.raw_material,
                        warehouse_id=warehouse_id
                    )
                except RawMaterialInventory.DoesNotExist:
                    raw_material_inventory = RawMaterialInventory.objects.create(
                        raw_material=raw_material.raw_material,
                        warehouse_id=warehouse_id,
                        quantity_on_hand=0,  # Set to the appropriate default value
                        unit_cost=0.0,  # Set to the appropriate default value
                        total_cost=0.0  # Set to the appropriate default value
                    )

                required_quantity = raw_material.quantity_required * quantity

                if raw_material_inventory.quantity_on_hand < required_quantity:
                    production_order.delete()  # Cancel the production order
                    return JsonResponse({'success': False, 'message': 'Not enough raw materials. Production order canceled.'})

                raw_material_inventory.quantity_on_hand -= required_quantity
                raw_material_inventory.total_cost -= (required_quantity * raw_material_inventory.unit_cost)
                raw_material_inventory.save()

        return JsonResponse({'success': True, 'message': 'Production order created successfully.'})

    def has_enough_raw_materials(self, product_id, quantity, warehouse_id):
        product = get_object_or_404(Product, pk=product_id)
        raw_materials = ProductRawMaterial.objects.filter(product=product)

        print("product_id:", product_id)
        print("quantity:", quantity)
        print("warehouse_id:", warehouse_id)

        for raw_material in raw_materials:
            try:
                raw_material_inventory = RawMaterialInventory.objects.get(
                    raw_material=raw_material.raw_material,
                    warehouse_id=warehouse_id
                )
            except RawMaterialInventory.DoesNotExist:
                raw_material_inventory = RawMaterialInventory.objects.create(
                    raw_material=raw_material.raw_material,
                    warehouse_id=warehouse_id,
                    quantity_on_hand=0,  # Set to the appropriate default value
                    unit_cost=0.0,  # Set to the appropriate default value
                    total_cost=0.0  # Set to the appropriate default value
                )

            required_quantity = raw_material.quantity_required * quantity

            if raw_material_inventory.quantity_on_hand < required_quantity:
                return False  # Not enough raw materials

        return True  # Enough raw materials
