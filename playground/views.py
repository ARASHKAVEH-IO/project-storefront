from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    
    querysete = Product.objects.filter(unit_price__range=(20 , 30))
    
    return render(request , 'hello.html' , {'name' : 'Arash' , 'products' : list(queryset)})