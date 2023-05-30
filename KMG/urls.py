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
from Shop import views 
from django.contrib import admin
from django.urls import path, include
from contact import urls
from Shop import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'),name='home'),
    path('shop/',include('Shop.urls'),name='shop'),
    path('contact/',include('contact.urls'),name='contact'),
   


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
