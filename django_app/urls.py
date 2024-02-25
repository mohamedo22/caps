from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('' , index , name='index'),
    path('login/' , login , name='login'),
    path('adminhome/' , adminhome , name='adminhome'),
    path('home/' , home , name='home'),
    path('Detils/' , detils , name='detils'),
    path('addflat/' , addflat , name='flat'),
]
