from django.shortcuts import render
from cart.models import cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import books
from django.contrib import messages
import sqlite3
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def search(request):

    id_list = []
    
    search = 'geography'

    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()

    #this is implicit, but there is no xxx row in my table, condition and something 
    #arent real parameters for my query

    qry=("select id from search_table where search_table match 'geography'" )
    c.execute(qry)

    

    print('++++++++++++++++++++++++++++++++++++++++')
    
    count = -1
    row = c.fetchall()
    if row == None:
        print('none')
        posts = None
        pass
    else:
        for x in row:
           
            row2 = int(x[count])
            print(row2)
           
            id_list.append(row2)
            count = count + 1

        print(id_list)
        rows = len(id_list)
        list2 = []

        print('size')
        print(rows)
        for x in range(1):
            posts = books.objects.filter(id__icontains = id_list[x])
        
    
    page = request.GET.get('page',1)

    paginator = Paginator(posts, 9)


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    
    context= {

        'posts' : posts,
       
        
    }

    return render(request, 'shop-grid.html', context)






def index(request):


    #categories on homescreen view

    dests_categoryall = books.objects.all()
    dests_categorybiographic = books.objects.filter(category = 'biographic')
    dests_categoryadventure = books.objects.filter(category = 'adventure')
    dests_categorykids = books.objects.filter(category = 'kids')
    dests_categorycook = books.objects.filter(category = 'cook')
    dest_relevant = books.objects.order_by("?")

    
    dests_categoryall_count = dests_categoryall.count()

    print('=====================')
    d = books.objects.filter(dec__icontains = 'g')
    print(d)

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

