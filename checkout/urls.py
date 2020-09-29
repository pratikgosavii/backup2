from django.urls import path, include

from . import views


urlpatterns=[

path('', views.checkout_page, name='checkout'),
path('placeorder', views.place_order, name='place_order'),
]