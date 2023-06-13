from django.db import models


class States(models.Model):
    state_name = models.CharField(max_length=255, unique=True)
    uf = models.CharField(max_length=2, unique=True) 