from django.db import models
from django.contrib.auth.models import User
from home.models import books
from checkout.models import user_address_detail, coupon_here
from django.conf import settings




# Create your models here.



class placedorder_book(models.Model):
    
    order_status_options = (
        
        (1, "order cancled"),
        (2, "complaint raise"),
        (3, "raise return"),
        (4, "return in progress"),
        (5, "return accepted"),
        (6, "return pickedup"),
        (7, "return order recevied"),
        (8, "return product quality check in progress"),
        (9, "return payment in progress"),
        (10, "return payment complete"),
        (11, "order is open"),
        (12, "order is accepted"),
        (13, "order packing"),
        (14, "out for delivery"),
        (15, "delivered"),
   
    )      

    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='product_buyerdfdfd', on_delete=models.CASCADE, default=1)
    placedorder_book = models.ForeignKey(books, related_name='buyer_who_buy_bookdfdf', on_delete=models.CASCADE, default=1)
    address = models.ForeignKey(user_address_detail, related_name='address_pointerdfdfd', on_delete=models.CASCADE, default=1)
    coupon = models.ForeignKey(coupon_here, related_name='books_which_user_buydfdf', on_delete=models.CASCADE, default=1)
    order_status = models.IntegerField(choices=order_status_options, default="order is open")
    quantity = models.IntegerField(default=1)
    date_time = models.DateTimeField()



    
