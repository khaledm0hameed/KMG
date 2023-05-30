from . import views
from django.urls import path


urlpatterns = [
    path('',views.send_massege,name='contact'),
]
