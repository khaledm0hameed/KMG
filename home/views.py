from django.shortcuts import render
from django.http import HttpResponse
from shop.models import category
# Create your views here.
def index (request):
    #return HttpResponse("HOME PAGE")
    return render(request,'home/index.html',{'cat':category.objects.all()})