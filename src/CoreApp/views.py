from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser  
from django.contrib.auth.hashers import make_password  
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.

def home(request):
    return render(request, 'home.html')

def logout_page(request):
    logout(request)
    return redirect('logout_page')

def user_login(request):
    if request.method == 'POST':
        id_no = request.POST.get('id')
        password = request.POST.get('password')
        
        if id_no == 'admin@sai' and password == 'admin123':
            return render(request, 'home.html')
        
        try:
            user = CustomUser.objects.get(id_no=id_no)
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid username')
            return redirect('user_login')
        
        authenticated_user = authenticate(username=id_no, password=password)
        
        if authenticated_user is None:
            messages.error(request, 'Invalid password')
            return redirect('user_login')
        
        login(request, authenticated_user)
        return redirect('home')
    
    return render(request, 'login.html')


import re

def password_check(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@!#$%])[A-Za-z\d@!#$%]{8,}$"
    return bool(re.match(pattern, password))

def register(request):
    if request.method == 'POST':
        id_no = request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        if not password_check(password):
            messages.error(request, 'Password must meet specific requirements')
            return redirect('register')
            
        if CustomUser.objects.filter(id_no=id_no).exists():
            messages.error(request, 'id_no number already taken')
            return redirect('register')
        
 
        user = CustomUser.objects.create_user(
            id_no=id_no,
            email=email,
            password = password,
        )
        
        messages.success(request, 'Successfully registered')
        print("Received username:", password)
    
    return render(request, 'register.html')


