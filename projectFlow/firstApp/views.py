from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MountainForm
from .models import Mountain

# Create your views here.

def home(request):
    return render(request, 'firstApp/home.html')

def market(request):
    return render(request, 'firstApp/market.html')


"CRUD on mountains"

def createMountain(request):
    form = MountainForm()

    if request.method == "POST":
        form = MountainForm(request.POST) # gets the data from what the user has input
        if form.is_valid():
            form.save()
            return redirect("readMountains")
            
    context = {"form": form}
    return render(request, "firstApp/form.html", context)

def readMountains(request):
    """
    - fetch data from DB
    - save data in context
    - pass data to template
    """

    mountains = Mountain.objects.all()
    context ={"mountains":mountains}
    return render(request, "firstApp/mountains.html", context)