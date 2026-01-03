from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    path('index3/', Index3, name='index3'),
    path('product/', Product, name='product'),
    path('checkout/', CheckOut, name='checkout'),
    path('contact/', Contact, name='contact'),
    path('shopping_cart/', Shopping_Cart, name='shopping-cart'),
]