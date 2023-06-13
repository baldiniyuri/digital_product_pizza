from django.db import models
from pizza.models import Pizza
from address.models import Address
from company.models import Company
from authentication.models import User


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    delivery_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)