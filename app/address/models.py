from django.db import models
from states.models import States
from counties.models import Counties


class Address(models.Model):
    street_address = models.CharField(max_length=255)
    city = models.ForeignKey(Counties, on_delete=models.CASCADE)
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=20)
    additional_instructions = models.TextField(blank=True, null=True)