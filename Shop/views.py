from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product
# Create your views here.
def productes(request):
    Pro=Product.objects.order_by('price') 
    return render(request, 'shop/shop.html',{'Pro':Pro})



def product_detail(request,id):
    obj=get_object_or_404(Product,pk=id)
    return render(request,'shop/detail.html',{'obj':obj})




