from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to your desired page
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already in use')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                login(request, user)
                return redirect('login')  # Redirect to your desired page
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'accounts/register.html')

def logout_user(request):
    logout(request)  # This logs out the user
    return redirect(reverse('login'))  # Redirect to login page after logout