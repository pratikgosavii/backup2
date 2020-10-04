from django.urls import path, include

from . import views


urlpatterns=[

path('', views.checkout_page, name='checkout'),
path('placeorder', views.place_order, name='place_order'),
path('placeorder_single', views.checkout_single_product, name='placeorder_single'),
]