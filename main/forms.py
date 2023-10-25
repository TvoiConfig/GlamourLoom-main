from django import forms
from .models import *

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['Product','date']