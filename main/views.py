from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Jidelnicek, Jidla

# Create your views here.

def home(response):
    return render(response,"main/base.html")

def ceny(response):
    return render(response,"main/ceny.html")

def food(response):
    return render(response,"main/food.html")

def formy(response):
    return render(response,"main/formy.html")

def training(response):
    return render(response,"main/training.html")

def food_user(response, id):
    ls = Jidelnicek.objects.get(id=id)
    return render(response,"main/food_user.html",{"ls":ls})

def onas(response):
    return render(response,"main/onas.html")

def zaregistrujse(response):
    return render(response,"main/zaregistrujse.html")
    
    
