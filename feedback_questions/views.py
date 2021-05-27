from django.shortcuts import render,  HttpResponseRedirect, reverse

# Create your views here.

from django.urls import reverse
from django.utils import timezone
import datetime
from django.contrib import messages
from .models import feedback, question
from home.models import books



# Create your views here.


def checkout_page(request):

    if request.user.is_authenticated:
        if request.method == 'POST':

            now = timezone.now()


        else:
            return render(request, 'error404')

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

            #step1 table1 
            #code for saving address (new address) 
          
            address_number = request.POST.get('address_number1')
            
            if address_number:
                pass
            
            else:

                form = user_address_detail_form(request.POST)
                print('-------------form 1 errors ----------')
                print(form.errors)
                if form.errors:
                    print('error bc')
                    return HttpResponseRedirect(reverse('checkout'))
                    
                    
                if form.is_valid():

                    instance = form.save(commit=False)

                    instance.save()
                else:
                    messages.warning(request, "you entered wrong information please try again or contact us at 8237377298.")
                    return HttpResponseRedirect(reverse('checkout'))
                    


            #step2  table2
            # collecting data for placedorder_book table



            if address_number:
                address_data = user_address_detail.objects.get(id = address_number)

            else:

                address_data_1 = user_address_detail.objects.filter(buyer = request.user)
                
                for x in address_data_1:
                    address_data_id = x.id
                
                address_data = user_address_detail.objects.get(id = address_data_id)

            

            #coupon code
            if request.session.get('coupon_applied', None) != None:

                coupon1 = request.session.get('coupon_name')
                coupon_data = coupon_here.objects.get(code = coupon1)

            else:

                coupon_data = coupon_here.objects.get(id = 1)
            book_id = request.POST['bookid']
            print(book_id)
            #coupon code end

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


            else:
                print(1)
                single_book_data = books.objects.get(id= book_id)
                address = address_data
                print('-----------')
                print(single_book_data)
                
                order_status = 1
                date_time = datetime.datetime.now()
                print('saving single atom')

                order_place = placedorder_book.objects.create(buyer = request.user, placedorder_book = single_book_data, address = address, coupon = coupon_data, order_status = order_status, date_time = date_time)
                order_place.save()
                messages.success(request, "your order is placed.")

            
            return HttpResponseRedirect(reverse('index'))
                


        else:
            return render(request, 'error404')

    else:
        messages.warning(request, "please login first!.")
        return HttpResponseRedirect(reverse('login_signup_home'))


def edit_address(request):

    if request.method == 'POST':

        editaddressid = request.POST['editaddressid']
        name = request.POST['name']
        mobilenumber = request.POST['mobilenumber']
        pincode = request.POST['pincode']
        address_full = request.POST['address_full']
        landmark = request.POST['landmark']
        addresstype = request.POST['addresstype']

        edit_data = user_address_detail.objects.get(id = editaddressid)
        edit_data.name = name
        edit_data.mobilenumber = mobilenumber
        edit_data.pincode = pincode
        edit_data.address_full = address_full
        edit_data.landmark = landmark
        edit_data.addresstype = addresstype

        edit_data.save()

        return HttpResponseRedirect(reverse('login_signup_home'))
            

            











#messages.info(request, 'This is the info messages!')
#messages.error(request, 'ERROR! ERROR!')
#messages.success(request, 'You registered succesfully')
#messages.warning(request, 'Be careful!')