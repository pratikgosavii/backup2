from django.db import models
from django.contrib.auth.models import User
from home.models import books
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime

# Create your models here.


class user_address_detail(models.Model):

    buyer = models.ForeignKey(User, related_name='buyer_product', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=225)
    mobilenumber = models.IntegerField()
    pincode = models.IntegerField()
    address_full = models.CharField(max_length=200)
    landamrk = models.CharField(max_length=200)
    addresstype = models.CharField(max_length=200, default="Home")
   
    
    def __str__(self):
        return self.name


class coupon_here(models.Model):

    code = models.CharField(max_length = 50, unique = True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()    

    def __str__(self):
        return self.code


class placedorder_book(models.Model):

    buyer = models.ForeignKey(User, related_name='product_buyer', on_delete=models.CASCADE, default=1)
    placedorder_book = models.ForeignKey(books, related_name='buyer_who_buy_book', on_delete=models.CASCADE, default=1)
    address = models.ForeignKey(user_address_detail, related_name='address_pointer', on_delete=models.CASCADE, default=1)
    coupon = models.ForeignKey(coupon_here, related_name='books_which_user_buy', on_delete=models.CASCADE, default=1)
    order_status = models.IntegerField()
    date_time = models.DateTimeField()
  
    
