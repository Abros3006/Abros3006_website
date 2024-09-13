from django.shortcuts import render, redirect
from django.contrib.auth import logout

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if already logged in
    return render(request, 'login.html')  # Render the login page

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout
