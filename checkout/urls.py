from django.urls import path, include

from . import views


urlpatterns=[

path('', views.checkout_page, name='checkout'),
path('checkout_singleproduct/<booki>', views.checkout_single_page, name='checkout_single'),

path('mobile_address', views.mobile_address, name='mobile_address'),
path('mobile_add_address', views.mobile_add_address, name='mobile_add_address'),
path('mobile_order_summary', views.mobile_order_summary, name='mobile_order_summary'),
path('mobile_payment', views.mobile_payment, name='mobile_payment'),

path('placeorder', views.place_order, name='place_order'),
path('mobile_placeorder', views.mobile_placeorder, name='mobile_placeorder'),
path('edit_saved_address', views.edit_address, name='edit_address'),
path('checkout_demo', views.checkout_demo, name='checkout_demo'),
]