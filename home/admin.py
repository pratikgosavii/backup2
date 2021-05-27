from django.contrib import admin
from .models import books, school_list, school_book

# Register your models here.




admin.site.register(books)
admin.site.register(school_list)
admin.site.register(school_book)