from typing import Reversible
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect



from home.models import books, school_book, school_list

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import ProductFilter
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView



# Create your views here.




def search(request):
    user_list = books.objects.all()
    posts = UserFilter(request.GET, queryset=user_list)
    return render(request, 'user_list.html', {'posts': posts})


def books_p(request):

    category = 'books_school'

    filter_standard = request.GET.get('std')
    filter_pattern  = request.GET.get('pat')
    value_3 = request.GET.get('sch')
    sort_by = request.GET.get('sortby')

    
    if filter_standard==None or filter_standard==None or filter_standard==None:

        pass




    try:
        school = school_list.objects.get(name=value_3)
        
    except:
        print('something went wrong')
        school = '1'
   
    
    

    if filter_standard == 'all' and filter_pattern != 'all':
        posts1 = school_book.objects.filter(standard = 'all', pattern =  filter_course, school_name = school)
        print('1')

    elif filter_standard != 'all' and filter_pattern == 'all':
        posts1 = school_book.objects.filter(standard = filter_standard, pattern =  'all', school_name = school)
        print('2')

    elif filter_standard == 'all' and filter_pattern == 'all':
        posts1 = school_book.objects.filter(standard = 'all', pattern =  'all', school_name = school)
        print('3')

    else:
        posts1 = school_book.objects.filter(standard = filter_standard, pattern = filter_pattern, school_name = school)

    
    if sort_by == 'price':

        print('in sort by')

        sort_by = 'book_name__' + sort_by
        posts1 = posts1.order_by(sort_by)
        
    if sort_by == '-price':
        
        posts1 = posts1.order_by('book_name__price')
        posts1= posts1.reverse()


   
    filter_data = ProductFilter(request.GET, queryset=posts1)
    
    posts = filter_data.qs

    books_count = posts.count()

    print('here count')
    
   
    
   
    page = request.GET.get('page',1)

    paginator = Paginator(posts, 9)

    


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


   

    context = {

        'grid_data' : posts,
        'filter_data' : filter_data,
        'study_filter_dropdown' : 'booksschool',
        'category' : 'books_school',
        'books_count' : books_count
    }
  
   

    return render(request, 'shop-grid.html', context)





def books_college_filter(request):

    if request.method == 'POST':
        standard = request.POST.get("standard")
        course  = request.POST.get("course")
       
       
 
        #session
        request.session['standard_college']= standard
        request.session['course_college']=course

    
    filter_standard=request.session['standard_college']
    filter_course= request.session['course_college']
    category  = 'books_college'
    

  
    if standard == 'all' and course != 'all':
       posts = books.objects.filter(standard = 'all', pattern =  filter_course, category = category)
       print('1')

    elif standard != 'all' and course == 'all':
        posts = books.objects.filter(standard = filter_standard, pattern =  'all', category = category)
        print('2')

    elif standard == 'all' and course == 'all':
        posts = books.objects.filter(standard = 'all', pattern =  'all', category = category)
        print('3')

    else:
        posts = books.objects.filter(standard = filter_standard, pattern = filter_pattern, category = category)
        print('4')
      
    
   
    page = request.GET.get('page',1)

    paginator = Paginator(posts, 9)

    


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    

        
    return render(request, '', {'posts': posts})


def books_eng_filter(request):

    if request.method == 'POST':
        year = request.POST.get("year")
        field  = request.POST.get("field")
       
       
 
        #session
        request.session['year_eng']= year
        request.session['field_eng']= field

    
    filter_year=request.session['year_eng']
    filter_field= request.session['field_eng']
    category  = 'books_eng'
    

  
    if year == 'all' and field != 'all':
       posts = books.objects.filter(standard = 'all', pattern =  filter_field, category = category)

    elif year != 'all' and field == 'all':
        posts = books.objects.filter(standard = filter_year, pattern =  'all', category = category)

    elif year == 'all' and field == 'all':
        posts = books.objects.filter(standard = 'all', pattern =  'all', category = category)

    else:
        posts = books.objects.filter(standard = filter_year, pattern = filter_field, category = category)
      
    
    
    page = request.GET.get('page',1)

    paginator = Paginator(posts, 9)


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    

        
    return render(request, 'shop-grid.html', {'posts': posts})


def books_medical_filter(request):

    if request.method == 'POST':
        year = request.POST.get("year")
        field  = request.POST.get("field")
       
       
 
        #session
        request.session['year_medical']= year
        request.session['field_medical']=field

    
    filter_year=request.session['year_medical']
    filter_field= request.session['field_medical']
    category  = 'books_medical'
    

  
    if year == 'all' and field != 'all':
       posts = books.objects.filter(standard = 'all', pattern =  filter_field, category = category)

    elif year != 'all' and field == 'all':
        posts = books.objects.filter(standard = filter_year, pattern =  'all', category = category)

    elif year == 'all' and field == 'all':
        posts = books.objects.filter(standard = 'all', pattern =  'all', category = category)

    else:
        posts = books.objects.filter(standard = filter_year, pattern = filter_field, category = category)
      
    
    
    page = request.GET.get('page',1)

    paginator = Paginator(posts, 9)


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    

        
    return render(request, 'shop-grid.html', {'posts': posts})

def single_product(request, b):

    dests = books.objects.filter(id = b)

    for dest in dests:

        standard = dest.standard
        pattern = dest.pattern


    dests_related = books.objects.filter(standard = standard, pattern = pattern).order_by("?")
    
    context= {

        'dests' : dests,
        'dests_related' : dests_related
    }

    return render(request, 'single-product.html', context)




def test(request):

    study_filter = request.GET.get('study_filter', 'None')

    posts1 = books.objects.all()

    filter_data = ProductFilter(request.GET, queryset=posts1)
    posts = filter_data.qs


    
    context = {

        'posts' : posts,
        'filter_data' : filter_data,
        'study_filter_dropdown' : study_filter_dropdown,
        'category' : category,
        'books_count' : books_count
        
    }
  


    return render(request, 'shop-grid_others.html', context)