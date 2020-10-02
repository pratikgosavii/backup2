from django.shortcuts import render,  HttpResponseRedirect, reverse

# Create your views here.

from cart.models import cart
import math
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse
from .forms import user_address_detail_form
from home.models import books
import datetime
from .models import user_address_detail, placedorder_book
from coupons.models import coupon
import pyrebase


# Create your views here.


def checkout_page(request):

    if request.user.is_authenticated:

        dests_checkout_products = cart.objects.filter(buyer = request.user)
        now = datetime.datetime.now()
        print('000000000000------------------------000000000')
        print(now)
        cart_count = 0
        cart_count = cart.objects.filter(buyer = request.user).count()

        cart_total = 0

        for dest in dests_checkout_products:

            cart_total = cart_total + int(dest.product_id.price)
        print('cart total')
        print(cart_total)

        if request.session.get('coupon_applied', None) != None:

            coupon_name = request.session.get('coupon_name')
            discount_amount = request.session.get('discount_amount')
            coupon_applied = request.session.get('coupon_applied')
            discount_amount = math.ceil(discount_amount)
            cart_total_afterdiscount = cart_total - discount_amount
        
        else: 
            cart_total_afterdiscount = cart_total
            discount_amount = None
            coupon_name = None
            coupon_applied = None

        saved_user_address = user_address_detail.objects.filter(buyer = request.user)
        print(saved_user_address)

        
        context= {

            'dests_checkout_products' : dests_checkout_products,
            'cart_count' : cart_count,
            'cart_total' : cart_total,
            'discount_amount' : discount_amount,
            'cart_total_afterdiscount' : cart_total_afterdiscount,
            'coupon_name' : coupon_name,
            'coupon_applied' : coupon_applied,
            'saved_user_address' : saved_user_address
            }

        return render(request, 'checkout.html', context)

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))




# code here for checkout insert daat into firebase must give name (placeorder_details) table


def place_order(request):

    if request.method == 'POST':
        if request.user.is_authenticated:

            #step1 table1 
            #code for saving address (new address)


            
            address_number = request.POST['address_number1']
            

            if address_number:
                pass
            
            else:

                form = user_address_detail_form(request.POST)
                print('-------------form 1 errors ----------')
                print(form.errors)
                if form.is_valid():

                    instance = form.save(commit=False)

                    buyer = request.user
                    instance.save()
                else:
                    return render(request, 'about.html')


            #step2  table2
            # collecting data for placedorder_book table



            if address_number:
                address_data = user_address_detail.objects.get(id = address_number)

            else:

                address_data_1 = user_address_detail.objects.filter(buyer = request.user)
                
                for x in address_data_1:
                    address_data_id = x.id
                
                address_data = user_address_detail.objects.get(id = address_data_id)

            book_data = cart.objects.filter(buyer = request.user)
            

            for x in book_data:
                
                data_in =  x.id
                print(data_in)
                placedorder_book_data1 = cart.objects.get(id = data_in)
                placedorder_book_data2 =  placedorder_book_data1.product_id.id
                placedorder_book_data = books.objects.get(id = placedorder_book_data2)
                address = address_data

                if request.session.get('coupon_applied', None) != None:

                    coupon1 = request.session.get('coupon_name')
                    coupon_data = coupon.objects.get(code = coupon1)

                else:

                    coupon_data = coupon.objects.get(code = 'none') 


                order_status = 1
                date_time = datetime.datetime.now()
                print('now i am here')
                order_place = placedorder_book.objects.create(buyer = request.user, placedorder_book = placedorder_book_data, address = address, coupon = coupon_data, order_status = order_status, date_time = date_time)
                order_place.save()
                print('and now here')
            return HttpResponseRedirect(reverse('login_signup_home'))
                

        else:

            return HttpResponseRedirect(reverse('login_signup_home'))

    else:

        print('something wents wrong')
        return HttpResponseRedirect(reverse('index'))

    
            

            





