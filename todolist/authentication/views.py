from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse


# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def logout(request):
    logout(request)  # This logs out the user
    return redirect(reverse('login'))  # Redirect to login page after logout