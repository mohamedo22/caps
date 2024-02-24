from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import *
from datetime import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request, 'index.html')
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        check = users.objects.get(email=email , password = password)
        check_admin = admins_s.objects.get(email=email , password = password)
        if check:
            return redirect(home)
        elif check_admin:
            return redirect(adminhome) 
        else:
            return render(request, 'login.html' , {'check':'false'})
    return render(request, 'login.html')
def home(request):
    all_flats = flats.objects.all()
    search = request.GET.get('search')
    s_f = flats.objects.filter(city=search).all()
    if s_f:
        return render(request, 'home.html', {'all_flats': s_f})
    return render(request, 'home.html', {'all_flats': all_flats})

@login_required(login_url='login')
def adminhome(request):
    return render(request , 'admin-home.html')
def detils(request):
    pk = request.GET.get('flatpk')
    flatcheck = flats.objects.filter(pk=pk).first()
    if flatcheck:
        images = flatcheck.flat_images_set.all() 
        return render(request , 'detils.html' , {'flat':flatcheck , 'images':images}) 
    return render(request , 'detils.html')