from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if username == 'admin@sai' and password == 'admin123':
            return render(request, 'home.html')
    
        if not User.objects.filter(username=username).exists():
             messages.error(request, 'InvalidNo username')
             return redirect('login')
    
        user = authenticate(username = username, password = password)
      
        if user is None:
            messages.error( request, 'InvalidNo password')
            return redirect('login')  
    
        else:
            login(request, user)
            return render(request, 'home.html')    
        
    return render(request, 'login.html')    

import re

def password_check(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@!#$%])[A-Za-z\d@!#$%]{12,}$"
    return bool(re.match(pattern, password))

def register(request):
    
    if request.method == 'POST':
        
        idNo = request.POST.get('id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, 'Password does not match')
            
        if password_check(password):
            messages.error(request, 'password must contain below mentioned characters')
            
        if username == '' or idNo == '' or email == '' or password == '':
            messages.error(request, 'Username is required')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        
        if User.objects.filter(idNo=idNo).exists():
            messages.error(request, 'idNo no. already taken')
            return redirect('register')    
        
        user = User.objects.create_user(
               idNo=idNo,
               username=username, 
               email=email,
               password=password, 
               confirm_password=confirm_password,
               )
        
        user.set_password(password)
        user.save()
        
        messages.success(request, 'successfully registered')
        
    
    return render(request, 'register.html')


