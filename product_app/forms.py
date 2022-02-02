from django import forms
from .models import *

class AddForm(forms.Form):
    # specify fields for model
    received_quantity = forms.CharField()

class SaleForm(forms.Form):
    # specify fields for model
    quantity = forms.IntegerField()
    amount_received = forms.IntegerField()
    issued_to = forms.CharField()
    

class newProductForm(forms.Form):
    # specify fields for model
    item_name = forms.CharField()
    category_name = forms.CharField()
    quantity = forms.IntegerField()
    unit_price = forms.IntegerField()

    