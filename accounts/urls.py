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

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [


    path('login_home', views.login_home, name='login_home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='loginn'),
    path('login_signup_home', views.loginsignuphome, name='login_signup_home'),
    path('logout', views.logout, name='logout'),
    path('login_firebase', views.login_firebase, name='login_firebase'),
    path('firebase_login_save', views.firebase_login_save, name='firebase_login_save'),
    path('change_password', views.change_password, name='change_password'),
    path('xxsdbwerg', views.set_password_html, name='set_password_html'),
    path('cdadhevgetgaeu', views.set_password_view, name='set_password_view'),



    


    path('', views.myaccount, name="my-account"),
    path('myorders', views.myorders, name="my-orders"),
    path('myaddress', views.myaddress, name="my-orders"),
    path('subscribe', views.subscibers_view, name='subscibers_view'),
    path('edit_user_info', views.edit_user_info, name='edit_user_info'),
    
    path('order_detials/<order_id>', views.order_detials, name='order_detials'),
   
   
    # path('', include('myorders.urls')),
]