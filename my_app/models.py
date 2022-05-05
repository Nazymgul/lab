from django.shortcuts import render
from django.db import models

# Create your models here.
class Information(models.Model):
    username = models.CharField(max_length=15,verbose_name="name")
    first_name = models.CharField(max_length=15,verbose_name="first_name")
    last_name = models.CharField(max_length=15,verbose_name="last_name")
    address = models.CharField(max_length=15,verbose_name="address")
    email =models.EmailField(blank = True)
    password1 =models.DecimalField(decimal_places=10,max_digits=100000000000,verbose_name="password")
    phone_number = models.IntegerField(verbose_name="phone_number")
class test(models.Model):
    username = models.CharField(max_length=15,verbose_name="name")
    first_name = models.CharField(max_length=15,verbose_name="first_name")

