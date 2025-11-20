from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def secondHome(request):
    return HttpResponse("Welcome to my Second Home!")