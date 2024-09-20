from django.shortcuts import render, redirect
from django.contrib.auth import logout

def login_view(request):
    return render(request, 'home')  # Render the login page

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout
