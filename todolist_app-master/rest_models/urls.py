from os import name
from django.contrib import admin
from django.urls import path,include
from .views import indexofrest,alltasks,taskX
appname = 'rest_models'
urlpatterns = [
    path('',indexofrest,name="index"),
    path('tasks/',alltasks,name="tasks"),
    path('detail/<str:pk>/',taskX,name="details"),
]
