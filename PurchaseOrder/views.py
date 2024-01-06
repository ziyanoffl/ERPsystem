from _decimal import Decimal
from django.shortcuts import render, redirect

from Inventory.models import RawMaterialInventory
from PurchaseOrder.forms import PurchaseOrderForm
from PurchaseOrder.models import PurchaseOrder


# Create your views here.
def create_purchase_order(request):
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            purchase_order = form.save()

            # Update RawMaterialInventory
            raw_material_inventory, created = RawMaterialInventory.objects.get_or_create(
                raw_material=purchase_order.raw_material,
                warehouse=purchase_order.warehouse
            )

            # Update unit_cost, total_cost, and last_updated
            raw_material_inventory.unit_cost = (
                Decimal(purchase_order.total_price) / purchase_order.quantity
            ) if purchase_order.quantity != 0 else Decimal(0.0)

            # Convert purchase_order.total_price to Decimal before adding
            raw_material_inventory.total_cost += Decimal(purchase_order.total_price)

            raw_material_inventory.last_updated = purchase_order.order_date
            raw_material_inventory.quantity_on_hand += purchase_order.quantity

            raw_material_inventory.save()

            return redirect('purchase_order_list')  # Redirect to a success page or another view
    else:
        form = PurchaseOrderForm()

    return render(request, 'Purchase Management/add_purchase_order.html', {'form': form})


def purchase_order_list(request):
    purchase_orders = PurchaseOrder.objects.all()
    return render(request, 'Purchase Management/view_purchase_orders.html', {'purchase_orders': purchase_orders})
