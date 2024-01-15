from django import forms

from Inventory.models import ProductRawMaterial
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'unit_price']


class ProductRawMaterialForm(forms.ModelForm):
    class Meta:
        model = ProductRawMaterial
        fields = ['raw_material', 'quantity_required']


ProductRawMaterialFormSet = forms.inlineformset_factory(Product, ProductRawMaterial, form=ProductRawMaterialForm,
                                                        extra=1)
