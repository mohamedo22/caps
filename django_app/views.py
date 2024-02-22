from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import *
from datetime import *
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')