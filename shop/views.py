from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def shop(request):
    return render(request,'shop/shop.html',{'pro':Product.objects.all()})