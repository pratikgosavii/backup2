from django.contrib.auth.models import User
import django_filters
from home.models import books



class ProductFilter(django_filters.FilterSet):

   
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = books
        fields = ['all_books', 'books_school', 'books_college', 'biographic', 'adventure', 'childern', 'cook', 'kids', 'other', 'popular', 'trending', 'bestseller' ,]

