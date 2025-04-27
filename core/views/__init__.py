from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='core:login')
def home(request):
    """Home page view"""
    return render(request, 'core/home.html') 