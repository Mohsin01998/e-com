from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50,null=True)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    digital=models.BooleanField(default=False,null=True,blank=False)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)


    def __str__(self):
        return self.name


class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True)
    date_order=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)


    def __str__(self):
        return str(self.id)


    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        items = [item.quantity for item in orderitems]
        return items

    @property
    def shipping(self):
        shipping=False
        orderitems=self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital==False:
                shipping=True
        return shipping

class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=0,null=True)



    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.address
