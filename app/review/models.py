from django.db import models
from pizza.models import Pizza
from company.models import Company


class Review(models.Model):
    customer_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    review_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
