from unicodedata import category
from django.db import models

# Create your models here.
class Expenses(models.Model):
    user_name = models.CharField(max_length=255),
    first_name = models.CharField(max_length=255),
    last_name = models.CharField(max_length=255),
    exp_category = models.CharField(max_length=255),
    exp_value = models.FloatField(max_length=100)