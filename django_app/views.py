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
    if search is not None:
        s_f = flats.objects.filter(city__icontains=search)
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
def addflat(request):
    if request.method=='POST':
        price = request.POST.get('price')
        bathnumbers = request.POST.get('bathnumbers')
        bedroomnumber = request.POST.get('bedroomnumber')
        gov = request.POST.get('gov')
        city = request.POST.get('city')
        floornumber = request.POST.get('floornumber')
        withf = request.POST.get('withf')
        phone = request.POST.get('phone')
        maini = request.FILES.get('mainimage')
        allim = request.FILES.getlist('images')
        if withf ==  "True":
            new_flat = flats(price=price , bathroomnumber = bathnumbers ,bedroomnumber=  bedroomnumber,gov=gov,city=city,floornumber=floornumber, with_f=True , active = False,phone=phone,mainimage=maini )
            new_flat.save()
        else:
            new_flat = flats(price=price , bathroomnumber = bathnumbers ,bedroomnumber=  bedroomnumber,gov=gov,city=city,floornumber=floornumber, with_f=False , active = False,phone=phone,mainimage=maini )
            new_flat.save()
        for img in allim:
            imge_f = flat_images(flat = new_flat , image=img )
            imge_f.save()
        return render(request , 'add-flat.html' , {'proccess':"true"})
    return render(request , 'add-flat.html')