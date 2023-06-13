from django.db import models
from states.models import States


class Counties(models.Model):
    county_name = models.CharField(max_length=255, unique=True)
    state = models.ForeignKey(States, on_delete=models.CASCADE)