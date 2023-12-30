from django.shortcuts import render, redirect, get_object_or_404

from .forms import WarehouseForm, RawMaterialForm
from .models import Warehouse, RawMaterial


# WQarehouse Management
def warehouse_management_view(request):
    warehouses = Warehouse.objects.all()
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warehouse_management_view')  # Redirect to a success page or another view
    else:
        form = WarehouseForm()
    context = {'form': form, 'warehouses': warehouses}
    return render(request, 'inventory/warehouse.html', context)


def warehouse_update(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)

    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            return redirect('warehouse_management_view')
    else:
        form = WarehouseForm(instance=warehouse)

    return render(request, 'inventory/warehouse_update.html', {'form': form, 'warehouse': warehouse})


def warehouse_delete(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)

    if request.method == 'POST':
        warehouse.delete()
        return redirect('warehouse_management_view')

    return render(request, 'inventory/warehouse.html', {'warehouse': warehouse})


# Raw material Mangement
def raw_material_view(request):
    raw_materials = RawMaterial.objects.all()
    if request.method == 'POST':
        form = RawMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warehouse_management_view')  # Redirect to a success page or another view
    else:
        form = RawMaterialForm()
    context = {'form': form, 'raw_materials': raw_materials}
    return render(request, 'inventory/raw_materials.html', context)
