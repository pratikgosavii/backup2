from django.shortcuts import render
from cart.models import cart
from django.contrib.auth.models import User
from .models import books



def extras(request):
    if request.user.is_authenticated:

        dests_usercart_home = cart.objects.filter(buyer=request.user)

        cart_count_home = cart.objects.filter(buyer = request.user).count()
    
        if cart_count_home == 0:
            cart_count_home = None
            subtotal_home = 0

            print('i am in dumass')

        

        else:

            subtotal_home = 0

            for dest in dests_usercart_home:
                subtotal_home = subtotal_home + int(dest.product_id.price)

           
           

    else:
        dests_usercart_home = None
        cart_count_home = None
        subtotal_home = 0


    context= {

        'cart_count_home' : cart_count_home,
        'dests_usercart_home' : dests_usercart_home,
        'totalprice' : subtotal_home,
    }

    return context