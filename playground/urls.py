from django.urls import path
from . import views

# url configuration module
urlpatterns = [
    path('hello/', views.say_hello)
]