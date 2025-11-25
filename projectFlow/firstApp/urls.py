from django.urls import path
from . import views

"""
    OBJECTIVE: 
    Create a CRUD application, Create..Read..Update..Delete
    - target will be Mountain table  
"""
urlpatterns = [ 
    path('', views.home),
    path('market', views.market),  
    path('create-mountain', views.createMountain, name="createMountain"),
    path('read-mountains', views.readMountains, name="readMountains"),
    ]
