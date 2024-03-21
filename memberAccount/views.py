from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import MyForm

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
            # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.success(request, f'Your account has been successfully created {username}..')
            return render(request, 'registration/login_message.html', {'error_message': 'Username is already taken. Please choose a different one.'})
            # Create the user
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()  
            return render(request, 'registration/login_user.html')
    
    return render (request, 'registration/signup.html', {})


'''def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, f'Login Sccessfully {username}..')
            return redirect('home')  # Change 'dashboard' to the URL name of your dashboard page
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid username or password.')
            return render(request, 'registration/login_message.html')  # Change 'login' to the URL name of your login page
    else:
        return render(request, 'registration/login_user.html')'''

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, f'Login Successfully {username}..')
            return redirect('home')  # Change 'dashboard' to the URL name of your dashboard page
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'registration/login_user.html', {'message': 'Invalid username or password.'})
    else:
        return render(request, 'registration/login_user.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out.')
    return redirect('home')

def login_message (request):
    return render(request, 'registration/login_message.html')