from django.shortcuts import render
from django.http import HttpResponse
from .forms import BottleForm

# Create your views here.

def home(request):
    return render(request, 'firstApp/home.html')

def market(request):
    return render(request, 'firstApp/market.html')


#CRUD OPERATIONS 

def createBottle(request):
    form = BottleForm()
    context = {} # data
    return render(request, context)


# def fetchBottles(request):
#     return render(request)