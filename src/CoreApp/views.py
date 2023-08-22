from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser  
from django.contrib.auth.hashers import make_password  


# Create your views here.


def home(request):
    return render(request, 'home.html')


def user_login(request):

    if request.method == 'POST':
        id_no = request.POST.get('id_no')
        password = request.POST.get('password')
    
        if id_no == 'admin@sai' and password == 'admin123':
            return render(request, 'home.html')
    
        if not CustomUser.objects.filter(id_no=id_no).exists():
             messages.error(request, 'Invalid username')
             return redirect('user_login')
    
        user = authenticate(username = id_no, password = password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('user_login') 
    
        else:
            login(request, user)
            return redirect('home')  
        
    return render(request, 'login.html')    

# import re

# def password_check(password):
#     pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@!#$%])[A-Za-z\d@!#$%]{12,}$"
#     return bool(re.match(pattern, password))

def register(request):
    if request.method == 'POST':
        id_no = request.POST.get('id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        # if not password_check(password):
        #     messages.error(request, 'Password must meet specific requirements')
        #     return redirect('register')
            
        if not (username and id_no and email and password):
            messages.error(request, 'All fields are required')
            return redirect('register')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')
        
        if CustomUser.objects.filter(id_no=id_no).exists():
            messages.error(request, 'ID number already taken')
            return redirect('register')
        
 
        user = CustomUser.objects.create(
            id_no=id_no,
            username=username, 
            email=email,
            password = password,
        )
        


        messages.success(request, 'Successfully registered')
        print("Received username:", password)
    
    return render(request, 'register.html')


