from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    context={}
    return render(request,'store.html',context=context)

def store(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'store.html',context=context)

def cart(request):
    context={}
    return render(request,'cart.html',context=context)

def checkout(request):
    context={}
    return render(request,'checkout.html',context=context)