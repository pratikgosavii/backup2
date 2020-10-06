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
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('login_signup_home', views.loginsignuphome, name='login_signup_home'),
    path('logout', views.logout, name='logout'),
    path('login_firebase', views.login_firebase, name='login_firebase'),
    path('home', views.home, name='home'),
    path('firebase_login_save', views.firebase_login_save, name='firebase_login_save'),
    path('', include('myorders.urls')),
]