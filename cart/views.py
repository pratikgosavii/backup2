from django.shortcuts import render,  HttpResponseRedirect, reverse
from .models import cart, wishlist
from home.models import books

# Create your views here.



def user_cart_addproduct(request):

    if request.user.is_authenticated:
        if request.method == 'POST':

            bookid = request.POST['bookid']


    
        producte = books.objects.get(id = bookid)

        obj = cart.objects.create(product_id = producte, buyer = request.user)

        obj.save()
        
    

        dests = cart.objects.filter(buyer = request.user)

        subtotal = 0
        for dest in dests:

            subtotal = subtotal + int(dest.product_id.price)

        context= {

                'dests' : dests,
                'totalprice' : subtotal
            }
    
   
   

        return render(request, 'cart.html', context)

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))


def user_cart_addproduct_byid(request, bookid):

 
    if request.user.is_authenticated:
        producte = books.objects.get(id = bookid)

        obj = cart.objects.create(product_id = producte, buyer = request.user)

        obj.save()
        
    

        dests = cart.objects.filter(buyer = request.user)

        subtotal = 0
        for dest in dests:

            subtotal = subtotal + int(dest.product_id.price)

        context= {

                'dests' : dests,
                'totalprice' : subtotal
            }

        return render(request, 'cart.html', context)


    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))
   
   

    


def user_cart(request):

    if request.user.is_authenticated:   
        dests = cart.objects.filter(buyer = request.user)

        context= {

                'dests' : dests,
                
            }

        return render(request, 'cart.html', context)

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))




def user_wishlist_addproduct(request, bookid):

   
    if request.user.is_authenticated:  
        producte = books.objects.get(id = bookid)

        obj = wishlist.objects.create(product_id = producte, buyer = request.user)

        obj.save()
        
        dests = wishlist.objects.filter(buyer = request.user)

        context= {

                'dests' : dests
                
            }

        return render(request, 'wishlist.html', context)

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))



def user_wishlist(request):

    if request.user.is_authenticated:
        dests = wishlist.objects.filter(buyer = request.user)

        context= {

                'dests' : dests
                
            }

        return render(request, 'wishlist.html', context)

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))


    


def remove_cartbook_byid(request, bookid):

    if request.user.is_authenticated:

        de = cart.objects.get(id = bookid)
        print('-----------------')
        print(de)
        de.delete()

        dests = cart.objects.filter(buyer = request.user)

        context= {

                'dests' : dests,
                
            }

        return render(request, 'cart.html', context)

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))



def remove_wishlistbook_byid(request, bookid):

    if request.user.is_authenticated:
        wishlist.objects.fiter(buyer = request.user, id = bookid).delete()

        wishlist.objects.fiter(buyer = request.user)

        context= {

                'dests' : dests,
                
            }

        return render(request, 'checkout.html', context)

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))


