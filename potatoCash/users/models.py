from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    logon_date = models.DateTimeField()
    permissions = models.CharField(max_length=255, default='user')