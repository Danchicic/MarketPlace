from django import forms
from .models import Order


class CreateOrderForm(forms.ModelForm):
    cart_id = forms.CharField(max_length=50)

    class Meta:
        model = Order
        fields = ('name', 'address', 'country', 'cart_id')
