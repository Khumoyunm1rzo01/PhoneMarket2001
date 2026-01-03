from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
import requests
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
# Create your views here.
def Index(request):
    slider = Slider.objects.all()
    product = Product_1.objects.all().order_by('-id')[0:5]
    context = {
        'slider': slider,
        'product': product,
    }
    return render(request, 'index.html', context)

def Index3(request):
    context = {
        
    }
    return render(request, 'index3.html', context)

def Product(request):
    product = Product_1.objects.all()
    context = {
       'product': product,
    }
    return render(request, 'product.html',  context)

def CheckOut(request):
    context = {
        
    }
    return render(request, 'checkout.html', context)

def Contact(request):
    context = {
        
    }
    return render(request, 'contact.html', context)

def Shopping_Cart(request):
    context = {
        
    }
    return render(request, 'shopping_cart.html', context)
