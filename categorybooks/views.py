from django.shortcuts import render
from home.models import books
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.



def categorybooks(request, name):

    posts = books.objects.filter(category = name)

    paginator = Paginator(posts, 9)

    page = request.GET.get('page')


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    

        
    return render(request, 'shop-grid.html', {'posts': posts})
