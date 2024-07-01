from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm

from payment.forms import ShippingForm
from payment.models import ShippingAddress

from django import forms
from django.db.models import Q
import json
from cart.cart import Cart

# Create your views here.

def update_info(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(request.POST or None ,instance = current_user)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Info has been updated")
            return redirect('home')
        return render(request , "update_info.html" ,{'form' :form})
    else:
        messages.success(request, "You must be Logged in to access thar Page!!")
        return redirect("home")
    



def category(request,foo):
    #Replace Hyphens with Spaces
    foo = foo.replace('-',' ')
    #Grab the category from the url
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html' , {'products': products} , {'category' : category})
    except:
        messages.success(request ,("That Category does not Exist..."))
        return render(request, 'home.html')
    


def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html', {'product':product})


def home(request):
    products = Product.objects.all()
    return render(request,'home.html', {'products':products})



def about(request):
    return render(request,'about.html' , {})



def login_user(request):
    if (request.method=="POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("You have logged in..."))
            return render(request, 'home.html',{})
        else:
           messages.error(request,"Invalid Credentials")
    else:
        return render(request,'login.html', {})

# def login_user(request):
#     if request.method == "POST":
#         username = request.POST.get('username')  # Safely get the username from POST data
#         password = request.POST.get('password')  # Safely get the password from POST data
#         if username and password:  # Ensure both username and password are provided
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "You have logged in...")
#                 return redirect('home')  # Redirect to home instead of calling home view directly
#             else:
#                 messages.error(request, "Invalid Credentials")
#         else:
#             messages.error(request, "Please enter both username and password")
#     return render(request, 'login.html', {})



def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out.....  Thank you"))
    return login_user(request)


def register_user(request):
    form = SignUpForm()
    if(request.method=="POST"):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #login user
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request,("You have Registered Successfully"))
            return redirect('home')
        else:
            messages.success(request,("Whoops! There was a error while Registering"))
            return render(request, 'register.html' , {})
    else:    
        return render(request,'register.html' , {'form':form})
    

