from django.shortcuts import render
from .models import coupon
from .forms import CouponApplyForm
from django.utils import timezone
from cart.models import cart
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.





def applycoupon(request):
    
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    print('1')
    if request.method == 'POST':
        print('2')
        if form.is_valid():
            print('3')
            code = form.cleaned_data['code']

            couponcheck = coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True)

            dests = cart.objects.filter(buyer = request.user)

            #calculating the total price of cart
            totalprice = 0
            for dest in dests:
                totalprice = totalprice + int(dest.product_id.price)

            #discount code
            if couponcheck:
                print('4')

                discount_percentage =  couponcheck.discount 
                
                print(discount_percentage)
                
                discount_amount =  ((totalprice / 100)* discount_percentage)
                print(discount_amount)
                request.session['coupon_name'] = code
                request.session['discount_amount'] = discount_amount
                request.session['couon_aplied'] = 'yes'


                return HttpResponseRedirect(reverse('checkout'))

            else:

                request.session['discount_amount'] = None
                request.session['coupon_aplied'] = None



                return HttpResponseRedirect(reverse('checkout'))
        else:
            
            return HttpResponseRedirect(reverse('checkout'))
    else:

        return render(request, 'error404.html')
