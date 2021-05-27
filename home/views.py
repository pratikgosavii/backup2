from django.shortcuts import render
from cart.models import cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import books, school_list
from django.contrib import messages
import math
import sqlite3
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_user_agents.utils import get_user_agent

# Create your views here.


def search(request):

    id_list = []
    posts = []
    
    search = request.GET.get('search')
    print(search)
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()

    qry=("select id from search_table where search_table match '{}'".format(search))

    c.execute(qry)

    row = c.fetchall()

    print('printinggggg row')
    print(row)

    

    
    for x in row:

        
        row2 = x[0]
       


        print(row2)
        
        id_list.append(row2)
        
        

    
    if row:

        for ids in id_list:
            posts12 = books.objects.filter(id = ids)

            posts.append(posts12)

            print(posts)
        print('here')
        
        print(posts)
            
        page = request.GET.get('page',1)

        paginator = Paginator(posts, 9)


        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        
        context= {

            'posts_searched' : posts,
        
            
        }

        return render(request, 'shop-grid.html', context)

        

        
    else:
        posts = None

    
    context= {

        'posts_searched' : posts,
    
        
    }
    

    return render(request, 'shop-grid.html', context)






def index(request):

    user_agent = get_user_agent(request)

    if user_agent.is_mobile:

        print('mobile')

    else:

        print('successfull')

    print('========================================================================')

    print(request.user)

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



    str = school_list.objects.all().order_by('id')
    school_names_count = str.count()

    school_names_count_div = school_names_count / 2


    splitat = math.ceil(school_names_count_div)
    l, r = str[:splitat], str[splitat:]

    print('----------------------------------------------')

    print(str)
    print(l)
    print(r)


    
    context= {

        'dests_categoryall_count' : dests_categoryall_count,
        'dests_categoryall' :  dests_categoryall,
        'dests_categorybiographic' : dests_categorybiographic,
        'dests_categoryadventure' : dests_categoryadventure,
        'dests_categorykids' : dests_categorykids,
        'dests_categorycook' : dests_categorycook,
        'dests_popular' :  dests_popular,
        'dest_relevant' : dest_relevant,
        'l' : l,
        'r' : r,
       
        
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



def view_404(request):

    return render(request, 'error404.html')