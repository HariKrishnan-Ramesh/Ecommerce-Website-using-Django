from django.shortcuts import redirect, render
from .models import Payment
from django import forms
from payment.forms import PaymentForm

# Create your views here.
def payment_success(request):
    return render(request, "payment/payment_success.html", {} )

def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # You need to create a success view and URL
    else:
        form = PaymentForm()
    return render(request, 'payments/payment.html', {'form': form})

def success_view(request):
    return render(request, 'payments/success.html')