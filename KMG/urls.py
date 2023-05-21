"""KMG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from home import urls
from shop import urls
from cart import urls
from login import urls
from myaccount import urls
from register import urls
from orderdetail import urls
from payment import urls
from django.contrib import admin
from django.urls import path, include
from contact import urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('shop/',include('shop.urls')),
    path('contact/',include('contact.urls')),
    path('login/',include('login.urls')),
    #path('myaccount/',include('myaccount.urls')),
    path('register/',include('register.urls')),
    #path('cart',include('cart.urls')),
    #path('orderdetail/',include('orderdetail.urls')),
    #path('payment',include('payment.urls')),
    
] + static(settings.MEDIA_URL,document_ROOT=settings.MEDIA_ROOT)
