from django.shortcuts import render
from home.models import books
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.



def categorybooks(request, name):

    #write if else here like:

    # if name == biograohic:
      #  posts = books.objects.filter(biographic = True)
    # elif name == kids:

    posts = books.objects.filter(name = True)
    paginator = Paginator(posts, 9)

    page = request.GET.get('page')

    print('-------------------------------------bb')
    print(posts)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    
    

        
    return render(request, 'shop-grid.html', {'posts': posts})
