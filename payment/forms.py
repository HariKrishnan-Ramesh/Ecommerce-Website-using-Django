from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['cardholder_name', 'card_number', 'expiration_date', 'cvv', 'amount']
        widgets = {
            'card_number': forms.TextInput(attrs={'placeholder': 'Card Number'}),
            'expiration_date': forms.DateInput(attrs={'placeholder': 'MM/YY'}),
            'cvv': forms.TextInput(attrs={'placeholder': 'CVV'}),
        }
