from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

from .models import Product
# Create your views here.
def productes(request):
    Pro=Product.objects.order_by('price') 
    return render(request, 'shop/shop.html',{'Pro':Pro})



def product_detail(request,id):
    obj=get_object_or_404(Product,pk=id)
    return render(request,'shop/detail.html',{'obj':obj})




@login_required(login_url="signin/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


@login_required(login_url="signin/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="signin/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="signin/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="signin/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart/shopping-cart.html")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/shopping-cart.html')








