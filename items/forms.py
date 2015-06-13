from django import forms
from items.models import Items


class CreateOrder(forms.ModelForm):
    model = Items
    pass