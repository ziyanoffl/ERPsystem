from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_code', 'product_name', 'description', 'unit_price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)