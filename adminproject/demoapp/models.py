from django.db import models
from unicodedata import name
# Create your models here.
class Drinks(models.Model):
    drinks = models.CharField(max_length=200)
    price = models.IntegerField()
class Drinks_category(models.Model):
    id = models.ForeignKey(Drinks, on_delete=models.PROTECT, default=None)
    drinks_category = models.CharField( max_length=50)
    price = models.IntegerField()
    