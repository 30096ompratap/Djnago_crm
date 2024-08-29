from django.shortcuts import render , redirect
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from .models import Record

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username = username ,password = password)
        if user is not None:
            login(request , user)
            messages.success(request,"logged in")
            return redirect('home')
        else:
            messages.success(request , "Please Try Again")
            return redirect ('home')
    else:
        return render(request,'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logout")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})

def customer_record(request):
    return render(request,'register.html',{})

def delete_record(request):
    return render(request,'register.html',{})

def add_record(request):
    return render(request,'register.html',{})

def update_record(request):
    return render(request,'register.html',{})
