from django import forms
from items.models import Order, Trash


class CreateTrash(forms.ModelForm):
    class Meta:
        model = Trash
        fields = ('count', 'number',)
        # number - may be not need TODO


class CreateOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('address', 'index', 'telephone',)


