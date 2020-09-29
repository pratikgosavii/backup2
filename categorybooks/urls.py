from django.urls import path, include

from . import views


urlpatterns=[

path('category<name>', views.categorybooks, name='categorybooks'),
]