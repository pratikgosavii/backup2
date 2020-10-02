from django.urls import path
from myorders import views

urlpatterns = [
    path('', views.myorders, name='my-orders')
]