from django.urls import path
from . import views

'''
    OBJECTIVE: 
    Create a CRUD application, Create..Read..Update..Delete
    - target will be Mountain table  
'''
urlpatterns = [ 
    path('', views.home, name='home'),
    path('market', views.market, name='market'),  
    path('create-mountain', views.createMountain, name='createMountain'),
    path('read-mountains', views.readMountains, name='readMountains'),
    path('read-one-mountain/<str:pk>', views.readOneMountain, name='readOneMountain'),
    path('update-one-mountain/<str:pk>', views.updateMountain, name='updateMountain'),
    path('delete-mountain/<str:pk>', views.deleteMountain, name='deleteMountain'),
    ]
