from unicodedata import category
from django.db import models

# Create your models here.
class Expenses(models.Model):
    username = models.CharField(max_length=255, default='test')
    firstname = models.CharField(max_length=255, default='test_fn')
    lastname = models.CharField(max_length=255, default='test_sn')
    expcategory = models.CharField(max_length=255, null=True, default='test_cat')
    expvalue = models.IntegerField()