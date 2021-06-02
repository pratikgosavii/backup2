from django.db import models
from django.contrib.auth.models import User
from home.models import books
from django.conf import settings

import datetime

# Create your models here.


class feedback(models.Model):

    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='maink', on_delete=models.CASCADE, default=1)
    feebdack_book = models.ForeignKey(books, related_name='feedback_product', on_delete=models.CASCADE, default=1)
    stars = models.IntegerField()
    feeback_title = models.CharField(max_length=200)
    feedback = models.CharField(max_length=200)
    
   
   

class question(models.Model):

    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='main', on_delete=models.CASCADE, default=1)
    question_book = models.ForeignKey(books, related_name='question_product', on_delete=models.CASCADE, default=1)
    question_title = models.CharField(max_length=200)
    question = models.CharField(max_length=200)
    
   
    
class feedback_reply(models.Model):

    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='replyxx', on_delete=models.CASCADE, default=1)
    feedback = models.ForeignKey(feedback, related_name='feedbadfdfck', on_delete=models.CASCADE, default=1)
    feedback_reply = models.CharField(max_length=200)


class question_reply(models.Model):

    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='replydfdq', on_delete=models.CASCADE, default=1)
    question = models.ForeignKey(question, related_name='qudfdfestion', on_delete=models.CASCADE, default=1)
    question_reply = models.CharField(max_length=200)
