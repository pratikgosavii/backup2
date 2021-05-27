"""admin1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [


    path('Cart_addproduct', views.user_cart_addproduct, name='user_cart_addproduct'),
    path('Cart_add_product_get<book_count>', views.Cart_addproduct_get, name='Cart_addproduct_get'),
    path('Cart_addproduct<bookid>', views.user_cart_addproduct_byid, name='user_cart_addproduct_byid'),
    path('add_Cart_from_wishlist<bookid>', views.add_Cart_from_wishlist, name='add_Cart_from_wishlist'),
    path('Cart', views.user_cart, name='user_cart'),

    path('Wishlist_addproduct<bookid>', views.user_wishlist_addproduct, name='user_wishlist_addproduct'),
    path('add_Wishlist_from_cart<bookid>', views.add_Wishlist_from_cart, name='add_Wishlist_from_cart'),
    path('Wishlist', views.user_wishlist, name='user_wishlist'),

    path('remove_cartbook_byid<bookid>', views.remove_cartbook_byid, name='remove_cartbook_byid'),
    path('remove_wishlistbook_byid<bookid>', views.remove_wishlistbook_byid, name='remove_wishlistbook_byid'),
   
]