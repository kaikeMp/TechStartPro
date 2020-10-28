from django.db import models
import pandas as pd

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
        
class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    value = models.DecimalField(decimal_places=2, max_digits=6)
    category = models.ManyToManyField(Category)
