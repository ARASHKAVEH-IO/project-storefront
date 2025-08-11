from django.shortcuts import render

from store.models import Customer


def say_hello(request):
     customer = Customer.objects.filter(first_name__icontains = "a")
    
     return render(request , 'hello.html' , {'name' : 'Arash' ,'customers': list(customer)})