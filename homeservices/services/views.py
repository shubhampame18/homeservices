from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


def admin_login(request):
    return render(request, 'admin_login.html')


def user_login(request):
    return render(request, 'user_login.html')


def contact(request):
    return render(request, 'contact.html')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        image = request.FILES.get('image')
        usertype = request.POST.get('usertype')
        print(fname,lname)

        user_info=CustomerUser(username=username,pwd=pwd,fname=fname,lname=lname,contact=contact,email=email,address=address,city=city,image=image,usertype=usertype)
        user_info.save()
    return render(request,'user_signup.html')


def services(request):
    return render(request, 'services.html')
