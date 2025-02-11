from django import forms
from django.core.exceptions import ValidationError
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'company', 'price', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['company'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        company = cleaned_data.get('company')
        price = cleaned_data.get('price')
        quantity = cleaned_data.get('quantity')

        if not name:
            raise ValidationError("Medicine name is required")
        if not company:
            raise ValidationError("Company name is required")
        if price <= 0:
            raise ValidationError("Price must be greater than zero")
        if quantity <= 0:
            raise ValidationError("Quantity must be greater than zero")

        return cleaned_data