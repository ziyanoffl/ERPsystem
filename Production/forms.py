from django import forms
from django.forms import inlineformset_factory

from Inventory.forms import ProductRawMaterialForm
from Inventory.models import ProductRawMaterial
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


ProductRawMaterialFormSet = inlineformset_factory(Product, ProductRawMaterial, form=ProductRawMaterialForm, extra=1,
                                                  can_delete=True)
