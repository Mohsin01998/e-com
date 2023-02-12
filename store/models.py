from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    digital=models.BooleanField(null=False)
    image=models.ImageField()

class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True)
    date_order=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(null=False)
    transaction_id=models.CharField(max_length=200,null=True)

class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    order=models.ForeignKey(Order,on_delete=models.DateTimeField,null=True)
    quantity=models.IntegerField(default=0,null=True)

class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

