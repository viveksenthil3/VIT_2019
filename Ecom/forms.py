from .models import customer_data
from django import forms


class CustomerRegisterationForm(forms.ModelForm):
    class Meta:
        model = customer_data
        fields = ('name', 'phone', 'location')

        field_order = {
            'name',
            'phone',
            'location',
        }