from django.shortcuts import render,  HttpResponseRedirect, reverse
from .models import cart, wishlist
from home.models import books

# Create your views here.



def user_cart_addproduct(request):

    if request.user.is_authenticated:
        if request.method == 'POST':

            bookid = request.POST.get('bookid')

            quantity = request.POST.get('quantity')
        
            producte = books.objects.get(id = bookid)

            if producte:

                try:
                    data = cart.objects.get(product_id = producte, buyer = request.user)
                except cart.DoesNotExist:
                    data = None

                if data:
                    if quantity:

                        quantity = int(quantity)
                        data.quantity =  quantity
                    else:
                        data.quantity = data.quantity + 1

                    data.save()
                else:
                    
                    obj = cart.objects.create(product_id = producte, buyer = request.user)
                    obj.save()
            else:
                return render(request, 'error404')


        else:
            return render(request, 'error404')


        


        return HttpResponseRedirect(reverse('user_cart'))

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))


def user_cart_addproduct_byid(request, bookid):

    if request.user.is_authenticated:

        try:
            producte = books.objects.get(id = bookid)

        except books.DoesNotExist:
            producte = None

        if producte:
    
            producte = books.objects.get(id = bookid)
            print('1')
            try:
                data = cart.objects.get(product_id = producte, buyer = request.user)
                print('2')

            except cart.DoesNotExist:
                data = None

            if data:
                data.quantity = data.quantity + 1
                data.save()
                print('3')

                
            else:
                obj = cart.objects.create(product_id = producte, buyer = request.user)
                print('4')

                obj.save()


            return HttpResponseRedirect(reverse('user_cart'))

        else:
            print('something went wrong')

            return HttpResponseRedirect(reverse('user_cart'))
            

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))


def add_Cart_from_wishlist(request, bookid):

    if request.user.is_authenticated:

        try:
            producte = books.objects.get(id = bookid)

        except books.DoesNotExist:
            producte = None

        if producte:
    
            try:
                data2 = wishlist.objects.get(product_id = producte, buyer = request.user).delete()
                print('2')

            except wishlist.DoesNotExist:
                data2 = None

            
            obj = cart.objects.create(product_id = producte, buyer = request.user)
            print('4')

            obj.save()


            return HttpResponseRedirect(reverse('user_cart'))

        else:
            print('something went wrong')

            return HttpResponseRedirect(reverse('user_cart'))
            

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))




def user_cart(request):

    if request.user.is_authenticated:   
        dests = cart.objects.filter(buyer = request.user)

        if dests:

            quantity = 0
            subtotal = 0
            for dest in dests:

                quantity = dest.quantity

                if quantity == 1:

                    subtotal = subtotal + int(dest.product_id.price)

                else:
                    subtotal = subtotal + (int(dest.product_id.price) * quantity)


            context= {

                    'dests' : dests,
                    'totalprice' : subtotal
                    
                }

            return render(request, 'cart.html', context)

        else:

            print('your art is empty')
            return render(request, 'cart.html')

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))



def Cart_addproduct_get(request, book_count):

    book_count_ = int(book_count)
    book_count_ = book_count_ + 1


    if request.user.is_authenticated:

        for i in range (1, book_count_):

            url_name = 'name'+str(i)
           
            bookid = request.GET.get(url_name)

            if bookid:

                try:
                    producte = books.objects.get(id = bookid)
                    print(producte)
                except books.DoesNotExist:
                    print('something went wrong')
                    data = None
                    producte = None
                    

                if producte:
                    

                    try:
                        data = cart.objects.get(product_id = producte, buyer = request.user)
                    except cart.DoesNotExist:
                        data = None

                    if data:

                        data.quantity = data.quantity + 1
                        data.save()


                    else:

                        obj = cart.objects.create(product_id = producte, buyer = request.user)
                        obj.save()
                

        print('=====yes')
        return HttpResponseRedirect(reverse('user_cart'))

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))



def user_wishlist_addproduct(request, bookid):

    if request.user.is_authenticated:  

        producte = books.objects.get(id = bookid)

        try:
            data = wishlist.objects.get(product_id = producte, buyer = request.user)
        except wishlist.DoesNotExist:
            data = None

        if data:

            data.quantity = data.quantity + 1
            data.save()

        else:

            obj = wishlist.objects.create(product_id = producte, buyer = request.user)

            obj.save()
        
       

        return HttpResponseRedirect(reverse('user_wishlist'))
        

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))




def add_Wishlist_from_cart(request, bookid):

    if request.user.is_authenticated:  


        try:
            producte = books.objects.get(id = bookid)

        except books.DoesNotExist:
            producte = None

        if producte:


            try:
                # data2 = cart.objects.get(product_id = producte, buyer = request.user).delete()
                print('2')

            except cart.DoesNotExist:
                data2 = None

            

            obj = wishlist.objects.create(product_id = producte, buyer = request.user)

            obj.save()
        
        

            return HttpResponseRedirect(reverse('user_wishlist'))

        else:
            print('something went wrong')
        

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

        cart.objects.get(id = bookid).delete()

        return HttpResponseRedirect(reverse('user_cart'))
        

    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))



def remove_wishlistbook_byid(request, bookid):

    if request.user.is_authenticated:
        wishlist.objects.get(buyer = request.user, id = bookid).delete()

        return HttpResponseRedirect(reverse('user_wishlist'))
        
    else:

	    return HttpResponseRedirect(reverse('login_signup_home'))






