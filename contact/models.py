from django.db import models

class Info(models.Model):
    Place=models.CharField(max_length=50,null=True , blank=True)
    Phone_number=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)

    

    class Meta:
        verbose_name = ("Info ")
        verbose_name_plural = ("Info s")

    def __str__(self):
        return self.email

   