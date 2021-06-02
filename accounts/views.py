import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from requests import request
from home.models import books
from myorders.models import user_address_detail, placedorder_book
from .models import subscibers
from home.models import books
from django.contrib.auth.models import User
import json


from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.


def login(request):
    if request.method == 'POST':

        
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email)

        print(password)


    
       
        user = auth.authenticate(username = email, password = password)


        if user is not None:
            auth.login(request, user)
            print('222222222222')

            return HttpResponseRedirect(reverse('index'))

        else:
            print('3333333333333')
            messages.error(request, ' invalid creddentils')
            return HttpResponseRedirect(reverse('login_home'))


    else:
        messages.warning(request, 'Somethings went wrong, contact us')
        return render(request, 'index.html')
        

def login_home(request):

    return render(request, 'login_home.html')



def loginsignuphome(request):

    a = request.GET.get('mobile_no')

    context= {
        
        'a': a
    }


    return render(request, 'loginsignup.html', context)


def register(request):
    if request.method == 'POST':
        email = request.POST['email']

        password1 = request.POST['password1']
        password2 = request.POST['password2']
        




        if password1 == password2 :

            if User.objects.filter(email = email).exists():
                messages.warning(request, 'Email exists ! Try to login ')
                return render(request, 'loginsignup.html')
           

            else:
                user = User.objects.create_user(  username = email, password = password1 )
                user.save()
                messages.success(request, 'register successful, login to start new trip with us !')
                return render(request, 'loginsignup.html')


        else:

            messages.warning(request, 'password does not match')
            return render(request, 'loginsignup.html')

    else:
        messages.warning(request, 'something went wrong, contact us')
        return render(request, 'loginsignup.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'You are now logout')
    return redirect('/')



def login_firebase(request):

    return render(request, 'login_firebase.html')

@csrf_exempt
def firebase_login_save(request):
    
    
    email=request.POST.get("email")
    provider=request.POST.get("provider")
    token=request.POST.get("token")
    mobile_login=request.POST.get("mobile_login")
    firbase_response=loadDatafromFirebaseApi(token)
    firbase_dict=json.loads(firbase_response)

    

    str = email
    print('here')
    splitat = 1
    l, r = str[:splitat], str[splitat:]
    r = '+'+r
    email=r   
    
    print(email)

    print('futt')


    if "users" in firbase_dict:
        user=firbase_dict["users"]
        if len(user)>0:
            
            print('1')

            user_one=user[0]
            if "phoneNumber" in user_one:
                if user_one["phoneNumber"]==email:
                    mobile_number = email
                    data=proceedToLogin(request,email, mobile_number)
                    print(data)

                    return HttpResponse(data)
                else:
                    print('print somethings went wrong')
                    return HttpResponse("Invalid Login Request")
           
            else:
                print('mobile not found')
                return HttpResponse("Unknown mobile User")                   
        else:
            return HttpResponse("Invalid Request User Not Found")
    else:
        print('user with this credential does not exists')  
        return HttpResponse("Bad Request")



def loadDatafromFirebaseApi(token):


    url = "https://identitytoolkit.googleapis.com/v1/accounts:lookup"

    payload = 'key=AIzaSyCywNPkHwl4_6YSFhKhheVVUHqPqKQE4mI&idToken='+token
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = request("POST", url, headers=headers, data=payload)

    return response.text



def proceedToLogin(request,email, mobile_number):

   


    users=User.objects.filter(mobile_number=email).exists()

    

    if users==True:
        print('exists')
        user_one=User.objects.get(mobile_number=email)
        user_one.backend='django.contrib.auth.backends.ModelBackend'
        auth.login(request,user_one)
        return "login_success"
    else:
        

       

        User.objects.create_user(email=None, mobile_number=email, password=settings.SECRET_KEY)
        user_one=User.objects.get(mobile_number=email)
      
        user_one.backend='django.contrib.auth.backends.ModelBackend'
        auth.login(request,user_one)
        request.session['mobile_no'] = email
        a = request.session['mobile_no']
     
        
        return "with new"

def set_password_html(request):

    return render(request, 'login_get_user_password.html')

def set_password_view(request):
    
    mob_data = request.session.get('mobile_no')
    
    password = request.POST.get('pasword')
    if mob_data:
        mob_data = str(mob_data)

        try:
            use = User.objects.get(mobile_number=mob_data)
        except User.DoesNotExist:
            print('something went wrong')
            return HttpResponseRedirect(reverse('login_home'))

        use.set_password(password) 
        use.save()
        auth.login(request,use)

        

        return HttpResponseRedirect(reverse('index'))


    else:
        print('something went wrong')
        return HttpResponseRedirect(reverse('login_home'))





def home(request):

    return HttpResponseRedirect(reverse('index'))

# def myaccount(request):
#     context = {
#         "accounts": "active",
#     }
#     return render(request, 'my-account/my-account.html', context)

def myorders(request):
   


    user_orders_open = placedorder_book.objects.filter(buyer = request.user, order_status = 2)
    user_orders_open1 = user_orders_open.count()
    print('count-----------------------1')
    print(user_orders_open1)
    user_orders_cancled = placedorder_book.objects.filter(buyer = request.user, order_status = 7).order_by('date_time')
    user_orders_all = placedorder_book.objects.filter(buyer = request.user).order_by('date_time')
    print(user_orders_all)
    user_orders_all1 = user_orders_all.count()
    print('zdnsjndj')
    print(user_orders_all)



    context= {
        
        'user_orders_open': user_orders_open,
        'user_orders_cancled': user_orders_cancled,
        'user_orders_all': user_orders_all
    }



    return render(request, 'my-account/my_orders.html', context)



def myaddress(request):

    saved_user_addresses = user_address_detail.objects.filter(buyer= request.user)

    context= {
        
        'saved_user_addresses' : saved_user_addresses,
        
    }

    print('jsgdsbdsfbfdfyeff--------------')
    print(saved_user_addresses)


    return render(request, 'my-account/my_address.html', context)



def subscibers_view(request):

    data = request.POST['subscibers_data']

    instance = subscibers.objects.create(data=data)

    instance.save()

    return HttpResponseRedirect(reverse('index'))
    

def myaccount(request):
    
    
    data = User.objects.filter()
    saved_user_addresses = user_address_detail.objects.filter(buyer= request.user)
    user_orders_open = placedorder_book.objects.filter(buyer = request.user, order_status = 2)
    user_orders_cancled = placedorder_book.objects.filter(buyer = request.user, order_status = 7).order_by('date_time')
    user_orders_all = placedorder_book.objects.filter(buyer = request.user).order_by('date_time')
    
    

    

    context= {
        
        'saved_user_addresses' : saved_user_addresses,
        'user_orders_open': user_orders_open,
        'user_orders_cancled': user_orders_cancled,
        'user_orders_all': user_orders_all
    }


    return render(request, 'my-account/my-account.html', context)
    

def edit_user_info(request):

    #request.post email1 = email

    if request.method == 'POST':

        email1 = request.POST.get('email')
        

        if User.objects.filter(email = email1).exists():

            #email already exsists
            print('email already exists please enter another email')
            return HttpResponseRedirect(reverse('my-account'))
            
        
        else:
            #edut the data

            mobilenumber = request.POST['editaddressid']
            name = request.POST['name']
            lastname = name.split(" ", 1)
            birthdate = request.POST['mobilenumber']
            alternatemobilenumber = request.POST['pincode']
            
            userid = request.user
            edit_data = User.objects.get(id = userid.id)

            if name:
                edit_data.first_name = name
            if mobilenumber:
                edit_data.mobilenumber = mobilenumber
            if lastname:
                edit_data.last_name = lastname
            if birthdate:
                edit_data.birthdate = birthdate
            if alternatemobilenumber:
                edit_data.alternate_mobile_number = alternatemobilenumber

            edit_data.save()

            print('data updated successfully')
            return HttpResponseRedirect(reverse('my-account'))

    else:

        print('somethofn wrnt eomf')
        return HttpResponseRedirect(reverse('index'))


    
def change_password(request):

    email = request.user.email

    password = request.POST.get('password')

    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if password1 == password2:

        user = User.objects.get(email = email, password = password)

        if user is not None:
    
            u = user.objects.get(email=email)
            u.set_password('password1')
            u.save()

        else:
            
            print('password incorrect')
            return HttpResponseRedirect(reverse('login_signup_home'))

    else:

        print('password does not match')
        return HttpResponseRedirect(reverse('login_signup_home'))
        


def loginsignupmobile(request):

    return render(request, 'mobilenumber.html')




def check_user_mobile(request):

    
    return render(request, 'login_with_password.html')
     


def order_detials(request, order_id):

    order_data = placedorder_book.objects.get(id = order_id)

    
    data = User.objects.filter()
    saved_user_addresses = user_address_detail.objects.filter(buyer= request.user)
    user_orders_open = placedorder_book.objects.filter(buyer = request.user, order_status = 2)
    user_orders_cancled = placedorder_book.objects.filter(buyer = request.user, order_status = 7).order_by('date_time')
    user_orders_all = placedorder_book.objects.filter(buyer = request.user).order_by('date_time')
    
    

    

    context= {
        
        'saved_user_addresses' : saved_user_addresses,
        'user_orders_open': user_orders_open,
        'user_orders_cancled': user_orders_cancled,
        'user_orders_all': user_orders_all,
        'order_data' : order_data,
    }


    return render(request, 'my-account/order_details.html', context)
    

