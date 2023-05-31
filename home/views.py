from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as auth_logout
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
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            email = user.first_email
            return render(request, 'home/index.html', {'email': email})
        else:
            messages.error(request, 'Bad creation')
            return redirect('signup')
    
    return render(request, 'accounts/login.html')





def logout(request):
    auth_logout(request)
    return redirect('/')

