from django.shortcuts import render,  HttpResponseRedirect, reverse

# Create your views here.

from cart.models import cart
import math
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse
from .forms import user_address_detail_form
from home.models import books
from myorders.models import placedorder_book
from django.utils import timezone
from django_user_agents.utils import get_user_agent
import datetime
from django.contrib import messages
from myorders.models import user_address_detail, placedorder_book
from django.contrib import messages
from .models import coupon_here
import pyrebase



# Create your views here.


def checkout_page(request):

    user_agent = get_user_agent(request)

    if user_agent.is_mobile:

        return HttpResponseRedirect(reverse('mobile_address'))

    else:

            

        if request.user.is_authenticated:

            now = timezone.now()

            if request.method == 'POST':
                applycoupon_code = request.POST.get('couponcheck')
                print(applycoupon_code)
                print('1')
                
            else:
                print('2')
                applycoupon_code = None

        
            dests_checkout_products = cart.objects.filter(buyer = request.user)
            cart_count = dests_checkout_products.count()
            
            

            # if checkout cart have product then
            if dests_checkout_products:
                cart_total = 0

                for dest in dests_checkout_products:

                    cart_total = cart_total + int(dest.product_id.price)

                if applycoupon_code:
                
                    couponcheck = coupon_here.objects.filter(code__iexact=applycoupon_code, valid_from__lte=now, valid_to__gte=now, active=True)
                    print('3')
                    if couponcheck:
                        print('4')
                        for couponcheck1 in couponcheck:
                            print('5')
                            request.session['coupon_name'] = couponcheck1.code
                            request.session['discount_amount'] = couponcheck1.discount
                            request.session['coupon_applied'] = 'yes'

                            discount_amount = couponcheck1.discount
                            coupon_name = couponcheck1.code
                            discount_amount = couponcheck1.discount
                            coupon_applied = 'yes'

                        # return this in context
                        cart_total_afterdiscount = cart_total - discount_amount


                #check of coupon session
                elif request.session.get('coupon_applied', None) != None:
                    print('kai kru')
                    coupon_name = request.session.get('coupon_name')
                    print(coupon_name)
                    couponcheck = coupon_here.objects.get(code__iexact=coupon_name, valid_from__lte=now, valid_to__gte=now, active=True)

                    if couponcheck:
                        #set sessions
                        coupon_name = request.session['coupon_name'] 
                        discount_amount = request.session['discount_amount'] 
                        coupon_applied = request.session['coupon_applied'] 

                        cart_total_afterdiscount = int(cart_total) - int(discount_amount)

                    else:
                        messages.warning(request, "your previously applies coupon is not applicable on this items.")
                        coupon_name = None
                        discount_amount = None
                        coupon_applied = None
                        cart_total_afterdiscount = cart_total
                    return HttpResponseRedirect(reverse('checkout'))


                #check for input checkout coupon code

                elif applycoupon_code:
                
                    couponcheck = coupon_here.objects.filter(code__iexact=applycoupon_code, valid_from__lte=now, valid_to__gte=now, active=True)
                    print('3')
                    if couponcheck:
                        print('4')
                        for couponcheck1 in couponcheck:
                            print('5')
                            request.session['coupon_name'] = couponcheck1.code
                            request.session['discount_amount'] = couponcheck1.discount
                            request.session['coupon_applied'] = 'yes'

                            discount_amount = couponcheck1.discount
                            coupon_name = couponcheck1.code
                            discount_amount = couponcheck1.discount
                            coupon_applied = 'yes'

                        # return this in context
                        cart_total_afterdiscount = cart_total - discount_amount

                    else:
                        # all values is none
                        coupon_name = None
                        discount_amount = None
                        coupon_applied = None
                        cart_total_afterdiscount = cart_total
                        messages.info(request, 'The coupon is invalid or expire')
                    return HttpResponseRedirect(reverse('checkout'))

                else:
                    print('4')
                    # all values is none
                    coupon_name = None
                    discount_amount = None
                    coupon_applied = None
                    cart_total_afterdiscount = cart_total


            else:
                messages.warning(request, "your cart is empty!.")
                return HttpResponseRedirect(reverse('user_cart'))

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

            messages.warning(request, "please login first!.")
            return HttpResponseRedirect(reverse('login_signup_home'))





def checkout_single_page(request, booki):

    if request.user.is_authenticated:

        now = timezone.now()
        productid = booki

        if request.method == 'POST':
            applycoupon_code = request.POST.get('couponcheck')
            print('here coupon')
           
        else:
            applycoupon_code = None

    
        dests_checkout_products = books.objects.get(id=productid)
        dests_checkout_products1 = books.objects.filter(id=productid)
        cart_count = 1
        
            

        # if checkout cart have product then
        if dests_checkout_products:   
            print('here')                                      
            cart_total = 0

           
            for dest in dests_checkout_products1:
                cart_total = dest.price

            #check for input checkout coupon code

            if applycoupon_code:
            
                couponcheck = coupon_here.objects.filter(code__iexact=applycoupon_code, valid_from__lte=now, valid_to__gte=now, active=True)

                if couponcheck:
                    for couponcheck1 in couponcheck:
                        request.session['coupon_name'] = couponcheck1.code
                        request.session['discount_amount'] = couponcheck1.discount
                        request.session['coupon_applied'] = 'yes'

                        discount_amount = couponcheck1.discount
                        coupon_name = couponcheck1.code
                        discount_amount = couponcheck1.discount
                        coupon_applied = 'yes'

                    # return this in context
                    cart_total_afterdiscount = int(cart_total) - int(discount_amount)

                else:
                    # all values is none
                    coupon_name = None
                    discount_amount = None
                    coupon_applied = None
                    cart_total_afterdiscount = cart_total
                    messages.info(request, 'The coupon is invalid or expire')
                    



            #check of coupon session
            elif request.session.get('coupon_applied', None) != None:
            
                coupon_name = request.session.get('coupon_name')
                try:
                    couponcheck = coupon_here.objects.get(code__iexact=coupon_name, valid_from__lte=now, valid_to__gte=now, active=True)
                    
                except coupon_here.DoesNotExist:
                    couponcheck = None

                if couponcheck:
                    #set sessions
                    coupon_name = request.session['coupon_name'] 
                    discount_amount = request.session['discount_amount'] 
                    coupon_applied = request.session['coupon_applied'] 

                    cart_total_afterdiscount = int(cart_total) - int(discount_amount)

                else:
                    messages.warning(request, "your previously applies coupon is not applicable on this items.")
                    coupon_name = None
                    discount_amount = None
                    coupon_applied = None
                    cart_total_afterdiscount = cart_total
                    
                  
                  


            else:
                # all values is none
                coupon_name = None
                discount_amount = None
                coupon_applied = None
                cart_total_afterdiscount = cart_total
            

        else:
            messages.warning(request, "something went wrong please try again.")
            return HttpResponseRedirect(reverse('index'))

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
            'saved_user_address' : saved_user_address,
            'productid' : productid
            }

        return render(request, 'checkout_single.html', context)
            
    else:

        messages.warning(request, "please login first!.")
        return HttpResponseRedirect(reverse('login_signup_home'))



def place_order(request):


    if request.user.is_authenticated:
        if request.method == 'POST':

            #use to identify is checkout is from cart or single checkout
            book_id = request.POST.get('bookid')

            #step1 table1 
            #code for saving address if new address option is selected (new address) 
          
            address_number = request.POST.get('address_number1')
            
            if address_number:
                print('address number2')
                pass
            
            else:

                form = user_address_detail_form(request.POST)
                print('-------------form 1 errors ----------')
                print(form.errors)
               
                    
                if form.is_valid():
                    print('valid')
                    instance = form.save(commit=False)
                    instance.buyer=request.user
                    instance.save()
                      
                else:
                   
                    messages.warning(request, "you entered wrong information please try again or contact us at 8237377298.")
                    return HttpResponseRedirect(reverse('checkout'))
                    


            #step2  table2
            # collecting data for placedorder_book table



            if address_number:
                address_data = user_address_detail.objects.get(id = address_number)
                print('addressnumber')

            else:

                address_data_1 = user_address_detail.objects.filter(buyer = request.user)
                print('------- =  = = ----')
                print(address_data_1)
            
                for x in address_data_1:
                    address_data_id = x.id
            
                address_data = user_address_detail.objects.get(id = address_data_id)

        

            #coupon code
            if request.session.get('coupon_applied', None) != None:

                coupon1 = request.session.get('coupon_name')
                coupon_data = coupon_here.objects.get(code = coupon1)

            else:

                coupon_data = coupon_here.objects.get(id = 1)
            
            print(book_id)
            #coupon code end

            #bokid is important here
            if book_id == 'cart_checkout':
                print('none')
                book_data = cart.objects.filter(buyer = request.user)
                for x in book_data:
                    data_in =  x.id
                    print(data_in)
                    placedorder_book_data1 = cart.objects.get(id = data_in)
                    placedorder_book_data2 =  placedorder_book_data1.product_id.id
                    placedorder_book_data = books.objects.get(id = placedorder_book_data2)
                    address = address_data

                    order_status = 1
                    date_time = datetime.datetime.now()
                    print('now i am here')
                    order_place = placedorder_book.objects.create(buyer = request.user, placedorder_book = placedorder_book_data, address = address, coupon = coupon_data, order_status = order_status, date_time = date_time)
                    order_place.save()
                    messages.success(request, "your order is placed.")
                    cart.objects.filter(buyer = request.user).delete()

                    return HttpResponseRedirect(reverse('index'))

                cart.objects.filter(buyer = request.user).delete()


            else:
                print(1)
                single_book_data = books.objects.get(id= book_id)
                address = address_data
                print('-----------')
                print(single_book_data)
                
                order_status = 1
                date_time = datetime.datetime.now()
                print('saving single item')

                order_place = placedorder_book.objects.create(buyer = request.user, placedorder_book = single_book_data, address = address, coupon = coupon_data, order_status = order_status, date_time = date_time)
                order_place.save()
                cart.objects.filter(buyer = request.user).delete()
                messages.success(request, "your order is placed.")
                return HttpResponseRedirect(reverse('index'))
                

            
            return HttpResponseRedirect(reverse('index'))
                


        else:
            return render(request, 'error404')

    else:
        messages.warning(request, "please login first!.")
        return HttpResponseRedirect(reverse('login_signup_home'))


def edit_address(request):

    user_agent = get_user_agent(request)

    if user_agent.is_mobile:

        if request.method == 'Get':

            #write code using get request

            editaddressid = request.POST['editaddressid']
            name = request.POST['name']
            mobilenumber = request.POST['mobilenumber']
            pincode = request.POST['pincode']
            address_full = request.POST['address_full']
            addresstype = request.POST['addresstype']

            edit_data = user_address_detail.objects.get(id = editaddressid)
            edit_data.name = name
            edit_data.mobilenumber = mobilenumber
            edit_data.pincode = pincode
            edit_data.address_full = address_full
            edit_data.addresstype = addresstype

            edit_data.save()

            return HttpResponseRedirect(reverse('mobile_address'))
        
        else:
            print('something went wrong')
            return HttpResponseRedirect(reverse('index'))
    
    else:
        
        if request.method == 'POST':

            editaddressid = request.POST['editaddressid']
            name = request.POST['name']
            mobilenumber = request.POST['mobilenumber']
            pincode = request.POST['pincode']
            address_full = request.POST['address_full']
            addresstype = request.POST['addresstype']

            edit_data = user_address_detail.objects.get(id = editaddressid)
            edit_data.name = name
            edit_data.mobilenumber = mobilenumber
            edit_data.pincode = pincode
            edit_data.address_full = address_full
            edit_data.addresstype = addresstype

            edit_data.save()

            return HttpResponseRedirect(reverse('login_signup_home'))

        else:
            print('something went wrong')
            return HttpResponseRedirect(reverse('index'))
            

            











#messages.info(request, 'This is the info messages!')
#messages.error(request, 'ERROR! ERROR!')
#messages.success(request, 'You registered succesfully')
#messages.warning(request, 'Be careful!')




def mobile_add_address(request):

    user_agent = get_user_agent(request)

    if user_agent.is_mobile:

        if request.user.is_authenticated:
            if request.method == 'POST':

                form = user_address_detail_form(request.POST)
                print('-------------form 1 errors ----------')
                print(form.errors)
                
                    
                if form.is_valid():
                    print('valid')
                    instance = form.save(commit=False)

                    instance.buyer=request.user
                    instance.save()

                    saved_user_address = user_address_detail.objects.filter(buyer = request.user)

                    context= {

                        'saved_user_address' : saved_user_address,
                        
                        }

                    return render(request, 'mobile_checkout/mobile_address.html', context)

                else:
                    
                    messages.warning(request, "you entered wrong information please try again or contact us at 8237377298.")
                    return HttpResponseRedirect(reverse('checkout'))
                
            else:
                    
                saved_user_address = user_address_detail.objects.filter(buyer = request.user)

                context= {

                    'saved_user_address' : saved_user_address,
                    
                    }

                return render(request, 'mobile_checkout/mobile_address.html', context)


        else:
            messages.warning(request, "please login first!.")
            return HttpResponseRedirect(reverse('login_signup_home'))

    
    else:

        return HttpResponseRedirect(reverse('checkout'))



    


def mobile_address(request):

    user_agent = get_user_agent(request)

    if user_agent.is_mobile:


        if request.user.is_authenticated:

            saved_user_address = user_address_detail.objects.filter(buyer = request.user)

            context= {

                'saved_user_address' : saved_user_address,
                
                }

            return render(request, 'mobile_checkout/mobile_address.html', context)

        else:
            messages.warning(request, "please login first!.")
            return HttpResponseRedirect(reverse('login_signup_home'))

    else:

        return HttpResponseRedirect(reverse('checkout'))



def mobile_order_summary(request):

    user_agent = get_user_agent(request)

    if user_agent.is_mobile:

        dests_checkout_products = cart.objects.filter(buyer = request.user)
        saved_user_address = user_address_detail.objects.filter(buyer = request.user).order_by('id').first()
        
        if request.method == 'POST':
            address_number = request.POST.get('address_number1')
        
        else:
            address_number = None

        

        if dests_checkout_products:

            if saved_user_address:

                if address_number:
                    request.session['checkout_address'] = address_number

                    

                    context= {

                        'dests_checkout_products' : dests_checkout_products
                    
                    }

                    
                    return render(request, 'mobile_checkout/mobile_order_summary.html', context)

                else:

                    if request.session['checkout_address'] != None:
                        
                        context= {

                            'dests_checkout_products' : dests_checkout_products
                    
                        }

                    
                        return render(request, 'mobile_checkout/mobile_order_summary.html', context)

                    else:

                        print('enter address first')
                        return render(request, 'mobile_checkout/mobile_address.html', context)
            
            else:
                print('enter your address')
                return render(request, 'mobile_checkout/mobile_address.html', context)


        else:

            print('your cart is empty')
            return HttpResponseRedirect(reverse('user_cart'))

    else:

        return HttpResponseRedirect(reverse('checkout'))


    



def mobile_payment(request):

    user_agent = get_user_agent(request)


    if user_agent.is_mobile:

        dests_checkout_products = cart.objects.filter(buyer = request.user)
        saved_user_address = user_address_detail.objects.filter(buyer = request.user).order_by('id').first()

        

        if dests_checkout_products:
            

            if saved_user_address: 

                if request.session['checkout_address'] != None:

                    saved_user_address_session = request.session['checkout_address']

                    address1 = user_address_detail.objects.filter(id = saved_user_address_session).first()

                    if address1:

                        demo = request.session['checkout_address']
                        print('address sessionnnnnnnnnnnnnnnnnnnnnnnnn')
                        print(demo)
                    

                        total_value = 0
                        for dest in dests_checkout_products:

                            total_value = total_value + int(dest.product_id.price)


                        context= {

                            'dests_checkout_products' : dests_checkout_products,
                            'total_value' : total_value,
                            
                            }

                        
                        return render(request, 'mobile_checkout/mobile_payment.html', context)

                    else:
                        print('session expire')
                        print('plzz enter your address')
                        return render(request, 'mobile_checkout/mobile_address.html', context)

                else:
                    
                    print('enter your address')
                    return render(request, 'mobile_checkout/mobile_address.html', context)


            else:

                print('enter your address')
                return render(request, 'mobile_checkout/mobile_address.html')
                

        else:

            print('your cart is empty')
            return HttpResponseRedirect(reverse('user_cart'))

    else:

        return HttpResponseRedirect(reverse('checkout'))


def mobile_placeorder(request):  

    dests_checkout_products = cart.objects.filter(buyer = request.user)
    saved_user_address = user_address_detail.objects.filter(buyer = request.user).order_by('id').first()  
    
    if dests_checkout_products:

        if saved_user_address: 

            if request.session['checkout_address'] != None:
    
                saved_user_address_session = request.session['checkout_address']

                address1 = user_address_detail.objects.filter(id = saved_user_address_session).first()

                if address1:
                

                    for x in dests_checkout_products:
                        data_in =  x.id
                    
                        placedorder_book_data1 = cart.objects.get(id = data_in)
                        quantity = placedorder_book_data1.quantity
                        placedorder_book_data2 =  placedorder_book_data1.product_id.id
                        placedorder_book_data = books.objects.get(id = placedorder_book_data2)
                        
                        address = address1
                        print(address)

                        order_status = 1
                        date_time = datetime.datetime.now()
                        coupon_data = coupon_here.objects.all().first()
                        order_place = placedorder_book.objects.create(buyer = request.user, placedorder_book = placedorder_book_data, address = address, quantity = quantity, coupon = coupon_data, order_status = order_status, date_time = date_time)
                        order_place.save()
                        messages.success(request, "your order is placed.")
                        cart.objects.filter(buyer = request.user).delete()

                        return HttpResponseRedirect(reverse('index'))

                    cart.objects.filter(buyer = request.user).delete()

                    return render(request, 'mobile_checkout/mobile_payment.html')

                else:
                    print('session expire')
                    print('plzz enter your address')
                    return render(request, 'mobile_checkout/mobile_address.html', context)


            else:
                
                print('enter your address')
                return render(request, 'mobile_checkout/mobile_address.html', context)


        else:

            print('enter your address')
            return render(request, 'mobile_checkout/mobile_address.html')
            

    else:

        print('your cart is empty')
        return HttpResponseRedirect(reverse('user_cart'))



def checkout_demo(request):

    return render(request, 'checkout_demo.html')