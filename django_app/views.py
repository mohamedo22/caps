from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from .models import *
from datetime import *
from django.core.mail import send_mail
from django.conf import settings
import random
from django_app import urls
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseBadRequest
def index(request):
    return render(request, 'index.html')
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == "oooomohamed421@gmail.com" and password == "Mohamed 12345678":
            return redirect(adminhome)
        try:
            check = users.objects.get(email=email , password = password)
            if check:
                return redirect(home)
        except ObjectDoesNotExist:
            return render(request, 'login.html' , {'check':'false'})
        try:
            check_admin = admins_s.objects.get(email=email , password = password)
            if check_admin:
                 return redirect(adminhome) 
        except ObjectDoesNotExist:
            return render(request, 'login.html' , {'check':'false'})
    return render(request, 'login.html')
def home(request):
    all_flats = flats.objects.filter(active=True)   
    search = request.GET.get('search')
    if search is not None:
        s_f = flats.objects.filter(city__icontains=search , active = True)
        return render(request, 'home.html', {'all_flats': s_f})
    return render(request, 'home.html', {'all_flats': all_flats})
def socailhouse(request):
    all_sc = social_house.objects.all()  
    return render(request, 'social_house.html', {'all_flats': all_sc})
@csrf_protect
def adminhome(request):
    all_flats = flats.objects.filter(active=False)
    all_sc = social_house.objects.all()
    if request.method=='POST':
        price = request.POST.get('price')
        bathnumbers = request.POST.get('bathnumbers')
        bedroomnumber = request.POST.get('bedroomnumber')
        city = request.POST.get('city')
        detils = request.POST.get('detils')
        phone = request.POST.get('phone')
        title = request.POST.get('title')
        mainimage = request.FILES.get('mainimage')
        allim = request.FILES.getlist('images')
        accept_p = request.POST.get('input_accept')
        new_social_house = social_house(downpayment=price,bathroomnumber=bathnumbers,bedroomnumber=bedroomnumber,detiels=detils,city=city,phone=phone,mainimage=mainimage , title=title)
        new_social_house.save()
        for img in allim:
            new_img= socialhouse_images(social_house = new_social_house , image = img)
            new_img.save()
            return render(request, 'admin-home.html', {'proccess': "true" , 'all_flats':all_flats , 'all_sc':all_sc})
    if request.method == 'GET':
        accept_p = request.GET.get('input_accept')
        deletep = request.GET.get('input_delete')
        if accept_p:
            try:
                flat = flats.objects.get(pk=accept_p)
                flat.active = True
                flat.save()
                return render(request, 'admin-home.html', {'proccess': "true" , 'all_flats':all_flats , 'all_sc':all_sc})
            except flats.DoesNotExist:
                return HttpResponseBadRequest("Flat with the provided ID does not exist.")
            except ValueError:
                return HttpResponseBadRequest("Invalid input for flat ID.")

        elif deletep:
            try:
                sc = social_house.objects.get(pk=deletep)
                sc.delete()
                return render(request, 'admin-home.html', {'proccess': "true" , 'all_flats':all_flats , 'all_sc':all_sc})
            except social_house.DoesNotExist:
                return HttpResponseBadRequest("Social house with the provided ID does not exist.")
            except ValueError:
                return HttpResponseBadRequest("Invalid input for social house ID.")
    return render(request , 'admin-home.html' , {'all_flats':all_flats , 'all_sc':all_sc}) 
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
def signup(request):
    if request.method=="POST":
       email = request.POST.get('email')
       password = request.POST.get('password')
       nationalid = request.POST.get('nationalid')
       code = random.randint(5000,10000)
       request.session['email'] = email
       request.session['password'] = password
       request.session['nationalid'] = nationalid
       request.session['code'] = code
       send_mail("Sign up code" , f'Your code is {code}' , settings.EMAIL_HOST_USER , [email], fail_silently=False)
       return redirect(confirmmail)
    return render(request,'sign_up.html')
def confirmmail(request):
    if request.method=="POST":
        email = request.session.get('email')
        password = request.session.get('password')
        nationalid = request.session.get('nationalid')
        code = request.session.get('code')
        codeuser = request.POST.get('codeus')
        if int(code) == int(codeuser):
            user = users(email=email,password=password,nationalid=nationalid)
            user.save()
            return redirect(home)
        else:
            return render(request, 'confirmmail.html' , {'check':'false'})
    return render(request , 'confirmmail.html')
