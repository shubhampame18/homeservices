from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import datetime


# Create your views here.
def index(request):
    return render(request, 'index.html')


def admin_login(request):
    return render(request, 'admin_login.html')


def user_login(request):
    error = ""
    if request.method =="POST":
        u=request.POST['uname'];
        p=request.POST['pwd'];
        user =authenticate(username=u, pwd=p)
        if user:
            try:
                user1 = CustomerUser.objects.get(user=user)
                if user1.type == "customer":
                    login(request, user)
                    error="no"
                else:
                    error="yes"
            except:
               error="yes"
        else:
            error="yes"
    d ={'error':error}
    return render(request, 'user_login.html', d)


def contact(request):
    return render(request, 'contact.html')


def Signup_User(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        e = request.POST['email']
        p = request.POST['pwd']
        con = request.POST['contact']
        add = request.POST['address']
        type = request.POST['type']
        im = request.FILES['image']
        dat = datetime.date.today()
        user = User.objects.create_user(email=e, username=u, password=p, first_name=f,last_name=l)
        if type=="customer":
            Customer.objects.create(user=user,contact=con,address=add,image=im)
        else:
            stat = Status.objects.get(status='pending')
            Service_Man.objects.create(doj=dat,image=im,user=user,contact=con,address=add,status=stat)
        error = "create"
    d = {'error':error}
    return render(request, 'signup.html', d)



def services(request):
    return render(request, 'services.html')

def user_home(request):
    if not request.user.is_authenticated:
        return  redirect('user_login')
    return render(request, 'user_home.html')