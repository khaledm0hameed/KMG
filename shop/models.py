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
    imge=models.ImageField(upload_to='photos/%y/%m/%d')
    description=models.TextField()
    categore=models.CharField(max_length=50,choices=choise,blank=True , null=True)

    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ['price']


 
