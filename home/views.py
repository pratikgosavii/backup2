from django.shortcuts import render
from cart.models import cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import books
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


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
    dests_categorybiographic = books.objects.filter(category = 'biographic')
    dests_categoryadventure = books.objects.filter(category = 'adventure')
    dests_categorykids = books.objects.filter(category = 'kids')
    dests_categorycook = books.objects.filter(category = 'cook')
    dest_relevant = books.objects.order_by("?")

    
    dests_categoryall_count = dests_categoryall.count()


    #popular on homescreen view
    dests_popular = books.objects.filter(popular = True)


    context= {

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

    return render(request, 'index.html', context)


    



def about(request):

    return render(request, 'about.html')


def contact(request):

    return render(request, 'contact.html')

def trending(request):


    posts = books.objects.filter(trending = True)

   
    page = request.GET.get('page',1)

    paginator = Paginator(posts, 9)



    

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    

        
    return render(request, 'shop-grid.html', {'posts': posts})


def bestseller(request):

    posts = books.objects.filter(bestseller = True)

    paginator = Paginator(posts, 9)

    page = request.GET.get('page')

    


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    

        
    return render(request, 'shop-grid.html', {'posts': posts})


def allproducts(request):

    posts = books.objects.all()

    paginator = Paginator(posts, 9)

    page = request.GET.get('page')

    


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    

        
    return render(request, 'shop-grid.html', {'posts': posts})

