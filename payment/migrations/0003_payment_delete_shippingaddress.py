# Generated by Django 5.0.6 on 2024-07-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_rename_address1_shippingaddress_shipping_address1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholder_name', models.CharField(max_length=100)),
                ('card_number', models.CharField(max_length=16)),
                ('expiration_date', models.DateField()),
                ('cvv', models.CharField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
