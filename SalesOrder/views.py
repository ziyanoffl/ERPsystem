# views.py
from django.contrib import messages
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from Inventory.models import ProductInventory
from Production.models import Product
from .forms import SalesOrderForm
from .models import SalesOrderItem, SalesOrder


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
                            messages.error(request,
                                           f"Insufficient quantity for product {product.product_name}. Order cancelled.")
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

            return redirect('product_inventory')  # Redirect to a success page after processing

    else:
        form = SalesOrderForm()
        products = Product.objects.all()
        context = {'form': form, 'products': products}

    return render(request, 'Sales Management/add_sales_order.html', context)


def sales_order_view(request):
    # Retrieve sales orders data from the database
    sales_orders = SalesOrder.objects.all()

    # Render the HTML template with the sales orders data
    return render(request, 'Sales Management/view_sales_orders.html', {'sales_orders': sales_orders})


def update_order_status(request, order_id):
    if request.method == 'POST':
        new_status = request.POST.get('status')

        # Get the SalesOrder instance or return a 404 response if not found
        order = get_object_or_404(SalesOrder, id=order_id)

        # Update the order status
        order.status = new_status
        order.save()

        # Redirect back to the sales order view
        return redirect('sales_order')
    else:
        return JsonResponse({'success': False})
