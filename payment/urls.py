from django.urls import path
from payment import views 
appname="payment"



urlpatterns = [
    path('payment/', views.payment_view, name='payment_view'),
    path('success/', views.success_view, name='success_view'),
]