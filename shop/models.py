from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=max)
    price=models.DecimalField(max_digits=50,decimal_places=3)
    imge=models.ImageField(upload_to='photos/%y/%m/%d')
    description=models.TextField()

