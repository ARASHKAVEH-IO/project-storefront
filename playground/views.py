from django.shortcuts import render
from store.models import Customer


def say_hello(request):
     
     customer = Customer.objects.order_by('first_name' , 'last_name')
    
     return render(request , 'hello.html' , {'name' : 'Arash' ,'customers': list(customer)})