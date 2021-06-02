from django.db import models
from django.contrib.auth.models import User
from home.models import books
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


import datetime

# Create your models here.


class user_address_detail(models.Model):

    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='buyer_product', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=225)
    mobilenumber = models.IntegerField()
    pincode = models.IntegerField()
    address_full = models.CharField(max_length=200)
    locality = models.CharField(max_length=200, default='akola')
    district = models.CharField(max_length=200, default='akola')
    addresstype = models.CharField(max_length=200, default="Home")
   
    


class coupon_here(models.Model):

    code = models.CharField(max_length = 50, unique = True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()    

