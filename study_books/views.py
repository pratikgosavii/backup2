from django.shortcuts import render, redirect
from home.models import books
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.






def books_study_filter(request):

    if request.method == 'POST':
        standard = request.POST.get("standard")
        pattern  = request.POST.get("pattern")
       
       
 
        #session
        request.session['standard_school']= standard
        request.session['patter_school']=pattern

    
    filter_standard=request.session['standard_school']
    filter_pattern= request.session['patter_school']
    category  = 'books_school'
    

  
    if standard == 'all' and pattern != 'all':
       posts = books.objects.filter(standard = 'all', pattern =  filter_pattern, category = category)

    elif standard != 'all' and pattern == 'all':
        posts = books.objects.filter(standard = filter_standard, pattern =  'all', category = category)

    elif standard == 'all' and pattern == 'all':
        posts = books.objects.filter(standard = 'all', pattern =  'all', category = category)

    else:
        posts = books.objects.filter(standard = filter_standard, pattern = filter_pattern, category = category)
      


    page = request.GET.get('page',1)

    paginator = Paginator(posts, 9)
    

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    

        
    return render(request, 'shop-grid.html', {'posts': posts})


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
        posts = books.objects.filter(standard = filter_standard, pattern = filter_course, category = category)
        print('4')
      
    
   
    page = request.GET.get('page',1)

    paginator = Paginator(posts, 9)

    


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    

        
    return render(request, 'shop-grid.html', {'posts': posts})


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

def single_product(request, book_id):

    dests = books.objects.filter(id = book_id)

    for dest in dests:

        standard = dest.standard
        pattern = dest.pattern


    dests_related = books.objects.filter(standard = standard, pattern = pattern).order_by("?")
    
    context= {

        'dests' : dests,
        'dests_related' : dests_related
    }

    return render(request, 'single-product.html', context)




