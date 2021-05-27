from django.shortcuts import render
from cart.models import cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from home.models import books
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    if request.user.is_authenticated:
        dests_usercart = cart.objects.filter(buyer=request.user)
        cart_count = cart.objects.filter(buyer = request.user).count()
        if cart_count == 0:
            cart_count = None
            subtotal = 0
            print('i am in dumass')
        else:
            subtotal = 0
            for dest in dests_usercart:
                subtotal = subtotal + int(dest.product_id.price)
    else:
        dests_usercart = None
        cart_count = None
        subtotal = 0

        #categories on homescreen view
        dests_categoryall = books.objects.all()
        dests_categorybiographic = books.objects.filter(biographic = True)
        dests_categoryadventure = books.objects.filter(adventure = True)
        dests_categorykids = books.objects.filter(kids = True)
        dests_categorycook = books.objects.filter(cook = True)
        dest_relevant = books.objects.order_by("?")
        dests_categoryall_count = books.objects.all().count()

        #popular on homescreen view
        dests_popular = books.objects.filter(popular = True)

        context = {
            'cart_count' : cart_count,
            'dests_categoryall_count' : dests_categoryall_count,
            'dests_usercart' : dests_usercart,
            'totalprice' : subtotal,
            'dests_categoryall' :  dests_categoryall,
            'dests_categorybiographic' : dests_categorybiographic,
            'dests_categoryadventure' : dests_categoryadventure,
            'dests_categorykids' : dests_categorykids,
            'dests_categorycook' : dests_categorycook,
            'dests_popular' :  dests_popular,
            'dest_relevant' : dest_relevant
        }
    return context