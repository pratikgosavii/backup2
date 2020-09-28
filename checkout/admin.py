from django.contrib import admin
from .models import placedorder_book, user_address_detail
# Register your models here.

admin.site.register(user_address_detail)
admin.site.register(placedorder_book)