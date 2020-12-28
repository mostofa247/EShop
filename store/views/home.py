from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import product
from store.models.category import Category
from django.views import View

# Create your views here.
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        #print(product)
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')
    
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        # return render(request, 'orders/order.html')
        categoryID = request.GET.get('category')
        if categoryID:
            products = product.get_all_products_by_categoryid(categoryID)
        else:
            products = product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print(request.session.get('email'))
        return render(request, 'index.html', data)
