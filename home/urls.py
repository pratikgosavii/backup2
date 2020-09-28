from django.urls import path, include

from . import views


urlpatterns=[

path('', views.index, name='index'),
path('contact', views.contact, name='contact'),
path('about', views.about, name='about'),

path('Trending', views.trending, name='trending'),
path('bestseller', views.bestseller, name='bestseller'),
path('allproducts', views.allproducts, name='allproducts'),

]