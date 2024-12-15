from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.firstname+self.lastname

class Order(models.Model):
    product=models.CharField(max_length=100)
    quantity=models.IntegerField()
    customer=models.ForeignKey(Customer,related_name='orders',on_delete=models.CASCADE)

