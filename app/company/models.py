from django.db import models
from address.models import Address
from pizza.models import Pizza


class Company(models.Model):
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    pizzas = models.ManyToManyField(Pizza, related_name='companies')