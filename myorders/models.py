from django.db import models
from django.contrib.auth.models import User
from home.models import books
from checkout.models import user_address_detail, coupon_here
from django.conf import settings




# Create your models here.



class placedorder_book(models.Model):
    
    order_status_options = (
        ("1", "order is open"),
        ("2", "order is accepted"),
        ("3", "order packing"),
        ("4", "out for delivery"),
        ("5", "delivered"),
        ("6", "order cancled"),
        ("7", "complaint raise"),
        ("8", "raise return"),
        ("9", "return in progress"),
        ("10", "return accepted"),
        ("11", "return pickedup"),
        ("12", "return order recevied"),
        ("13", "return product quality check in progress"),
        ("14", "return payment in progress"),
        ("15", "return payment complete"),
   
    )      

    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='product_buyerdfdfd', on_delete=models.CASCADE, default=1)
    placedorder_book = models.ForeignKey(books, related_name='buyer_who_buy_bookdfdf', on_delete=models.CASCADE, default=1)
    address = models.ForeignKey(user_address_detail, related_name='address_pointerdfdfd', on_delete=models.CASCADE, default=1)
    coupon = models.ForeignKey(coupon_here, related_name='books_which_user_buydfdf', on_delete=models.CASCADE, default=1)
    order_status = models.CharField(max_length=50, choices=order_status_options, default="order is open")
    quantity = models.IntegerField(default=1)
    date_time = models.DateTimeField()