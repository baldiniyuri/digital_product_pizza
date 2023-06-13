from django.db import models
from pizza.models import Pizza
from address.models import Address


class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    delivery_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)