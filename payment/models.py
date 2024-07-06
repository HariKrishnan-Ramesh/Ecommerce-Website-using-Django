from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Payment(models.Model):
    cardholder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment from {self.cardholder_name} for {self.amount}"