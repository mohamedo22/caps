from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import *
from datetime import *
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    return render(request, 'index.html')
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        check = users.objects.get(email=email , password = password)
        if check:
            return redirect(home)
        else:
            return render(request, 'login.html' , {'check':'false'})
    return render(request, 'login.html')
def home(request):
    return render(request , 'home.html')