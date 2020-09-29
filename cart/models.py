from django.db import models
from django.contrib.auth.models import User
from home.models import books

# Create your models here.


class cart(models.Model):

    product_id =models.ForeignKey(books, related_name='books', on_delete=models.CASCADE, default=1)
    buyer = models.ForeignKey(User, related_name='buyer', on_delete=models.CASCADE, default=1)



class wishlist(models.Model):

    product_id =models.ForeignKey(books, related_name='bookswishlist', on_delete=models.CASCADE, default=1)
    buyer = models.ForeignKey(User, related_name='buyerwishlist', on_delete=models.CASCADE, default=1)

