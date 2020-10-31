from django.urls import path, include

from . import views


urlpatterns=[

path('', views.checkout_page, name='checkout'),
path('checkout_singleproduct/<booki>', views.checkout_single_page, name='checkout_single'),
path('placeorder', views.place_order, name='place_order'),
]