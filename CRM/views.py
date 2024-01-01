from django.shortcuts import render, redirect, get_object_or_404

from CRM.forms import CustomerForm, SupplierForm
from CRM.models import Customer, Supplier


#######################################
# Customer Management #################
#######################################
def customer_management_view(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_management_view')  # Redirect to a success page or another view
    else:
        form = CustomerForm()
    context = {'form': form, 'customers': customers}
    return render(request, 'CRM/view_customer.html', context)


def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_management_view')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'CRM/update_customer.html', {'form': form, 'customer': customer})


#######################################
# Supplier Management #################
#######################################
def supplier_management_view(request):
    suppliers = Supplier.objects.all()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_management_view')  # Redirect to a success page or another view
    else:
        form = SupplierForm()
    context = {'form': form, 'suppliers': suppliers}
    return render(request, 'CRM/view_supplier.html', context)


def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)

    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('customer_management_view')
    else:
        form = SupplierForm(instance=supplier)

    return render(request, 'CRM/update_supplier.html', {'form': form, 'supplier': supplier})
