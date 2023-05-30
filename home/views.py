from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def index (request):
    #return HttpResponse("HOME PAGE")
    return render(request,'home/index.html')



def signup (request):


   if request.method == "POST":
      name = request.POST['name']
      email = request.POST['email']
      password1 = request.POST['password']
      password2=request.POST['password2']

      myuser= User.objects.create_user(name,email,password1)
      myuser.first_name=name
      myuser.last_name=name

      myuser.save()
      return redirect('signin')


   return render(request,'accounts/register.html')

def signin(request):
    return render(request,'accounts/login.html')

def logout(request):
   pass