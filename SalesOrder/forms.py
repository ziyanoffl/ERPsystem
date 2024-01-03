# forms.py
from django import forms
from django.forms import formset_factory

from .models import SalesOrder, SalesOrderItem

class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['customer', 'order_date', 'ship_date', 'status', 'total_price']
        widgets = {
            'order_date': forms.DateInput(attrs={'type': 'date'}),
            'ship_date': forms.DateInput(attrs={'type': 'date'}),
        }
