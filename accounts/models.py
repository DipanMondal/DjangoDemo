from django.db import models

# Create your models here.


class Admin(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)


class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)