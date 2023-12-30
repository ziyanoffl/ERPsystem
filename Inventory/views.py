from django.shortcuts import render, redirect

from .forms import WarehouseForm


# Create your views here.
def warehouse_management_view(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warehouse_management_view')  # Redirect to a success page or another view
    else:
        form = WarehouseForm()
    return render(request, 'inventory/warehouse.html', {'form': form})
