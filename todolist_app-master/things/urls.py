from django.contrib import admin
from django.urls import path,include
from .views import index
appname = 'things'
urlpatterns = [
    path('',index,name="index")
]

