from django import forms
from .models import Item


class Itemform(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["item_name", "item_decription", "item_price", "item_price_currency", "item_image"]
