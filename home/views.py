from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        
        # Send email
        send_mail(
            f'New contact form submission: {subject}',
            f'Name: {name}\nEmail: {email}\nMessage: {subject}',
            email,
            ['atharva.bangle@mitwpu.edu.in'],
            fail_silently=False,
        )
        
        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('home')
    
    return render(request, 'index.html')