from django.forms import modelformset_factory
from django.shortcuts import render, redirect

from Inventory.forms import ProductRawMaterialForm
from Inventory.models import ProductRawMaterial, RawMaterial
from .forms import ProductForm, ProductRawMaterialFormSet
from .models import Product


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
