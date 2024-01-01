from django import forms
from django.forms import inlineformset_factory

from Inventory.models import Warehouse, RawMaterial, ProductRawMaterial
from Production.models import Product


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class RawMaterialForm(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductRawMaterialForm(forms.ModelForm):
    class Meta:
        model = ProductRawMaterial
        fields = ['raw_material', 'quantity_required']
