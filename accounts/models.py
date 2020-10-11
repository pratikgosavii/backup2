from django.db import models


# Create your models here.


class subscibers(models.Model):

    data = models.CharField(max_length=200, default="Home")
   
    
    def __str__(self):
        return self.data
