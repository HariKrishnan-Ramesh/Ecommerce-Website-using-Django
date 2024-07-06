from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment_view, name='payment_view'),
    path('success/', views.success_view, name='success_view'),
]