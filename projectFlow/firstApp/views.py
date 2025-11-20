from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'firstApp/home.html')

def market(request):
    return render(request, 'firstApp/market.html')
