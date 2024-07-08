from django.urls import path
from payment import views 
app_name="payment"



urlpatterns = [
    path('payment/', views.payment_view, name='payment'),
    path('success/', views.success_view, name='success'),
]