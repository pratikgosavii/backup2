from django.shortcuts import render
from cart.models import cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import books
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):


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

        'dests_categoryall_count' : dests_categoryall_count,
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

    #yaha e agar koi book na mile toh message dikhana hai scrren ke uper alert ma nhi

   
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

