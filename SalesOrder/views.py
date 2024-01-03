# views.py
from django.contrib import messages
from django.db import transaction
from django.db.models import Sum
from django.shortcuts import render, redirect

from Inventory.models import ProductInventory, Warehouse
from Production.models import Product
from .forms import SalesOrderForm
from .models import SalesOrderItem


def add_sales_order(request):
    if request.method == 'POST':
        form = SalesOrderForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # Create SalesOrder instance
                    sales_order = form.save()

                    # Process sales order items
                    product_ids = request.POST.getlist('product[]')
                    quantities = request.POST.getlist('product_quantity[]')

                    cancel_order = False

                    for product_id, quantity in zip(product_ids, quantities):
                        product = Product.objects.get(pk=product_id)
                        unit_price = product.unit_price  # Replace with the actual field in your Product model
                        total_price = unit_price * int(quantity)

                        # Check if there is sufficient quantity in the inventory
                        product_inventory = ProductInventory.objects.get(product=product)
                        if int(quantity) > product_inventory.quantity_on_hand:
                            messages.error(request, f"Insufficient quantity for product {product.product_name}. Order cancelled.")
                            cancel_order = True
                            break

                        # Create SalesOrderItem instance
                        SalesOrderItem.objects.create(
                            order=sales_order,
                            product=product,
                            quantity=quantity,
                            unit_price=unit_price,
                            total_price=total_price
                        )

                        # Update product inventory
                        product_inventory.quantity_on_hand -= int(quantity)
                        product_inventory.save()

                    if cancel_order:
                        # Rollback changes and cancel the order
                        raise Exception("Order cancellation due to insufficient quantity")

            except Exception as e:
                # Handle any exceptions and notify the user
                messages.error(request, f"An error occurred: {str(e)}")
                return redirect('error_page')  # Redirect to an error page

            return redirect('success_page')  # Redirect to a success page after processing

    else:
        form = SalesOrderForm()
        products = Product.objects.all()
        context = {'form': form, 'products': products}

    return render(request, 'Sales Management/add_sales_order.html', context)
