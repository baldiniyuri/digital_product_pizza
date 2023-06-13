from django.contrib.auth.models import AbstractUser
from django.db import models
from address.models import Address


class User(AbstractUser):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=9)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
