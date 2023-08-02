from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate


# Create your views here.


def register(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        if password == confirm_password:
            User.objects.create(email=email, password=password, full_name = full_name ,phone_number=phone_number)
        else:
            context['error'] = "Passwords do not equal"
        
    return render(request, 'main/register.html', context)



def auth(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists() and User.objects.filter(password=password).exists:
            context['good'] = 'Your accont has in database'
        else:
            context['errors'] = "You need to register in site"
        
    
    return render(request, 'main/auth.html',context)


   