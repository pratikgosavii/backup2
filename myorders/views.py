from django.shortcuts import render

# Create your views here.

def myorders(request):
    return render(request, 'my-orders/index.html', context={})