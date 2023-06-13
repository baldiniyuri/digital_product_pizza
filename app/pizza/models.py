from django.db import models


class Pizza(models.Model):
    flavor = models.CharField(max_length=255)
    second_flavor = models.CharField(max_length=255, null=True, blank=True, default=None)
    is_two_flavors = models.BooleanField(default=False)