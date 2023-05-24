from django.db import models

class Product(models.Model):
    choise=[
        ('Laptop','Laptop'),
        ('Computer','Computer'),
        ('Phone','Phone'),
        ('Screen','Screen'),
    ]
    name=models.CharField(max_length=300)
    price=models.DecimalField(max_digits=50,decimal_places=3)
    imge=models.ImageField(upload_to='photos/%y/%m/%d',default='photos/unknow.jpg')
    description=models.TextField()
    category=models.CharField(max_length=100,null=True,choices=choise)

    def __str__(self,):
        return self.name
    

    class Meta:
        ordering = ['price']
