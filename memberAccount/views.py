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
           # return HttpResponse('Username is already taken. Please choose a different one.')
            return render(request, 'registration/login.html', {'error_message': 'Username is already taken. Please choose a different one.'})
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()  
        #return HttpResponse('Sign up successful! You can now log in.')
        return render(request, 'registration/login.html')
        
    return render (request, 'registration/signup.html', {})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
    else:
        form = AuthenticationForm()
    return render (request, 'registration/login.html', {'form': form})
