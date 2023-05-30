from django.urls import path
from . import views

urlpatterns = [
    path('', views.productes, name='Shop'),
    path('<int:id>',views.product_detail,name='detail')
    
    # other URL patterns...
]
