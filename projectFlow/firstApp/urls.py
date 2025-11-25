from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home),
    path('market', views.market), 
    
    # CRUD Operations
    path('create-bottle', views.createBottle, name='createBottle'),
    path('bottles', views.fetchBottles, name='fetchBottles')
]
