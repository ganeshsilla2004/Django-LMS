from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser

def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        id_no = request.POST.get('id')
        password = request.POST.get('password')
        
        if id_no == 'admin@sai' and password == 'admin123':
            return redirect('home')
        
        try:
            user = CustomUser.objects.get(id_no=id_no)
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid username')
            return redirect('user_login')
        
        authenticated_user = authenticate(request, username=id_no, password=password)
        
        if authenticated_user is None:
            messages.error(request, 'Invalid password')
            return redirect('user_login')
        
        login(request, authenticated_user)
        return redirect('home')
    
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        id_no = request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        if CustomUser.objects.filter(id_no=id_no).exists():
            messages.error(request, 'ID number already taken')
            return redirect('register')
        
        user = CustomUser.objects.create_user(id_no=id_no, email=email, password=password)
        messages.success(request, 'Successfully registered')
        
    return render(request, 'register.html')

@login_required
def protected_view(request):
    return render(request, 'protected.html')
