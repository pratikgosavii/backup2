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
import json
# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
       

        user = auth.authenticate(username = email, password = password)

        if user is not None:
            auth.login(request, user)

            return HttpResponseRedirect(reverse('index'))

        else:
            messages.error(request, ' invalid creddentils')
            return render(request, 'loginsignup.html')

    else:
        messages.warning(request, 'Somethings went wrong, contact us')
        return render(request, 'loginsignup.html')



def loginsignuphome(request):
    return render(request, 'loginsignup.html')


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
    
    username=request.POST.get("username")
    email=request.POST.get("email")
    provider=request.POST.get("provider")
    token=request.POST.get("token")
    firbase_response=loadDatafromFirebaseApi(token)
    firbase_dict=json.loads(firbase_response)


    if "users" in firbase_dict:
        user=firbase_dict["users"]
        if len(user)>0:
            user_one=user[0]
            if "phoneNumber" in user_one:
                if user_one["phoneNumber"]==email:
                    data=proceedToLogin(request,email, username, token, provider)
                    return HttpResponse(data)
                else:
                    print('print somethings went wrong')
                    return HttpResponse("Invalid Login Request")
            else:
                if email==user_one["email"]:
                    provider1=user_one["providerUserInfo"][0]["providerId"]
                    if user_one["emailVerified"]==1 or user_one["emailVerified"]==True or user_one["emailVerified"]=="True" or provider1=="facebook.com":
                        data=proceedToLogin(request,email,username,token,provider)
                        return HttpResponse(data)
                    else:
                        print('Please Verify Your Email to Get Login')
                        return HttpResponse("Please Verify Your Email to Get Login")
                else:
                    print('email not found')
                    return HttpResponse("Unknown Email User")
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



def proceedToLogin(request,email,username,token,provider):

    users=User.objects.filter(username=username).exists()

    if users==True:
        user_one=User.objects.get(username=username)
        user_one.backend='django.contrib.auth.backends.ModelBackend'
        auth.login(request,user_one)
        return "login_success"
    else:
        user=User.objects.create_user(username=username,email=email,password=settings.SECRET_KEY)
        user_one=User.objects.get(username=username)
        user_one.backend='django.contrib.auth.backends.ModelBackend'
        auth.login(request,user_one)
        return "login_success"



def home(request):

    return HttpResponseRedirect(reverse('index'))

def myaccount(request):
    return render(request, 'my-account/my-account.html', context={})
