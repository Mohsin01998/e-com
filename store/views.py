from django.shortcuts import render
from .models import Product,Order
# Create your views here.

def home(request):
    context={}
    return render(request,'store.html',context=context)

def store(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'store.html',context=context)

def cart(request):
    if request.method=='POST':
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem.set_all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        # cartItems = order['get_cart_items']
    context={'items':items,'order':order}
    return render(request,'cart.html',context=context)

def checkout(request):
    context={}
    return render(request,'checkout.html',context=context)