from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import memberRegister
from .forms import MyForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            #return HttpResponse('Username is already taken. Please choose a different one.')
            return render(request, 'registration/login.html', {'error_message': 'Username is already taken. Please choose a different one.'})
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()  
        #return HttpResponse('Sign up successful! You can now log in.')
        return render(request, 'registration/login.html')
    
    return render (request, 'registration/signup.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #login(request, user)
            return render(request, 'home')
            return HttpResponse("Login successful!")  # You can replace this with your desired response
        else:
            return HttpResponse("Invalid username or password")

    return render(request, 'registration/login.html')


