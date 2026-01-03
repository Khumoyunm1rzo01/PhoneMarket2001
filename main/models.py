from django.db import models

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=255)
    sale = models.TextField(null=True, blank=True)
    phonename = models.CharField(max_length=255)
    about = models.TextField()
    image = models.FileField(upload_to='media/slider')
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    
class Product_1(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/Images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_1 = models.CharField(max_length=255, null=True, blank=True)
    price_2 = models.CharField(max_length=255)
    sale = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)