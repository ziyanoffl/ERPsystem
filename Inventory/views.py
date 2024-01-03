from django.shortcuts import render, redirect, get_object_or_404

from .forms import WarehouseForm, RawMaterialForm
from .models import Warehouse, RawMaterial, RawMaterialInventory


# Warehouse Management
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


#####################################
# Raw material Management
#####################################
def raw_material_view(request):
    raw_materials = RawMaterial.objects.all()
    if request.method == 'POST':
        form = RawMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('raw_material_view')  # Redirect to a success page or another view
    else:
        form = RawMaterialForm()
    context = {'form': form, 'raw_materials': raw_materials}
    return render(request, 'inventory/raw_materials.html', context)


def raw_material_update(request, pk):
    raw_materials = get_object_or_404(RawMaterial, pk=pk)

    if request.method == 'POST':
        form = RawMaterialForm(request.POST, instance=raw_materials)
        if form.is_valid():
            form.save()
            return redirect('raw_material_view')
    else:
        form = RawMaterialForm(instance=raw_materials)

    return render(request, 'inventory/raw_material_update.html', {'form': form, 'raw_materials': raw_materials})


def raw_material_inventory_list(request):
    raw_material_list = RawMaterialInventory.objects.all()
    return render(request, 'inventory/view_available_raw_materials.html',
                  {'raw_material_inventory_list': raw_material_list})


#####################################
# Product Management
#####################################

def create_product(request):
    if request.method == 'POST':
        form = RawMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('raw_material_view')  # Redirect to a success page or another view
    else:
        form = RawMaterialForm()
    context = {'form': form}
    return render(request, 'inventory/raw_materials.html', context)
