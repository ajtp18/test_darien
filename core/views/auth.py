from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('core:login') 