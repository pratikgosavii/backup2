from django.db import models

# Create your models here.


class books(models.Model):


     

    all_books = models.BooleanField(default= False)
    books_school = models.BooleanField(default= False)
    books_college = models.BooleanField(default= False)
    books_engineering = models.BooleanField(default= False)
    books_medical = models.BooleanField(default= False)

    biographic = models.BooleanField(default= False)
    adventure = models.BooleanField(default= False)
    childern = models.BooleanField(default= False)
    cook = models.BooleanField(default= False)
    other = models.BooleanField(default= False)
    kids = models.BooleanField(default= False)
    
    popular = models.BooleanField(default= False)
    trending = models.BooleanField(default= False)
    bestseller = models.BooleanField(default= False)
    new = models.BooleanField(default= False)
    InStock = models.BooleanField(default= True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    dec = models.CharField(max_length=50)
    standard = models.CharField(max_length=50)
    pattern = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    bookfront_cover = models.ImageField(upload_to='pics',default='picc')
    bookback_cover = models.ImageField(upload_to='pics',default='picc')
    index_1 = models.ImageField(upload_to='pics',default='picc')
    index_2 = models.ImageField(upload_to='pics',default='picc')
    index_3 = models.ImageField(upload_to='pics',default='picc')
    index_4 = models.ImageField(upload_to='pics',default='picc')







class school_list(models.Model):

    name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50, default='noel')
    school_image = models.ImageField(upload_to='pics',default='picc')





class school_book(models.Model):

    book_name = models.ForeignKey(books, related_name='books_for_school', on_delete=models.CASCADE, default=1)
    school_name = models.ForeignKey(school_list, related_name='school', on_delete=models.CASCADE, default=1)
    standard = models.CharField(max_length=50)
    pattern = models.CharField(max_length=50)




