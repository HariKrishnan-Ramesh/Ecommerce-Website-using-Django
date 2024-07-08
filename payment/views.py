from django.shortcuts import redirect, render
from .models import Payment
from django import forms
from payment.forms import PaymentForm

# Create your views here.


def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"success.html")  # You need to create a success view and URL
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')