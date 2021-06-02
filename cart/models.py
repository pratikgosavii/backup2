from django.db import models
from home.models import books
from django.conf import settings

# Create your models here.


class cart(models.Model):

    product_id =models.ForeignKey(books, related_name='books', on_delete=models.CASCADE, default=1)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='buyer', on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default = 1)



class wishlist(models.Model):

    product_id =models.ForeignKey(books, related_name='bookswishlist', on_delete=models.CASCADE, default=1)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='buyerwishlist', on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default = 1)
