from django.urls import path
from myorders import views

urlpatterns = [
    path('my-orders', views.myorders, name='my-orders')
]