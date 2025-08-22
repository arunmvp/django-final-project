from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate


# Create your views here.


# def home(request):
#     return render(request, "main.html")


# def shop(request):
#     return render(request, "shop.html")


def signup(request):
    return render(request, "signup.html")


def loginview(request):
    return render(request, "login.html") 


def pro_page(request):
    dataproducts = feature_products.objects.filter(price__lt = 100) 
    newproducts = feature_products.objects.filter(price__gt = 100)
    return render(request , 'main.html' , {'products': dataproducts, 'newproducts': newproducts}) 

def shop_page(request):
    shopproducts = feature_products.objects.all()
    return render(request, 'shop.html' , {'allproducts' : shopproducts})

def signupFun(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname") 
        lastname = request.POST.get("lastname")
        userName = request.POST.get("username") 
        Email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")
        if password == confirmpassword:
            if User.objects.filter(username=userName).exists():
                return redirect("Signup")
            elif User.objects.filter(email=Email).exists(): 
                return redirect("Signup")
            else:
                user = User.objects.create_user(
                    first_name=firstname,
                    last_name=lastname,
                    username=userName,
                    email=Email,
                    password=password,
                )
                user.save() 
                
                
                return redirect("Home") 
        else:
            return redirect("Signup")
    else:
        return redirect("Signup")
    

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect("Home")
        else:
            return redirect("Login")
        
    else:
        return redirect("Login")
            
            