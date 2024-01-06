from django import forms

from .models import SalesOrder


class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['customer', 'order_date', 'ship_date', 'status', 'total_price']
        widgets = {
            'order_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'style': 'width: 33.33%'}),
            'ship_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'style': 'width: 33.33%'}),
            'customer': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 33.33%'}),
            'status': forms.Select(attrs={'class': 'form-select', 'style': 'width: 33.33%'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 33.33%'}),
        }
        labels = {
            'order_date': 'Order Date',
            'ship_date': 'Ship Date',
            'total_price': 'Total Price',
        }
        choices = (
            ('pending', 'Pending'),
            ('shipped', 'Shipped'),
        )
        widgets['status'] = forms.Select(choices=choices, attrs={'class': 'form-select', 'style': 'width: 33.33%'})
