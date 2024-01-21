from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def register (request):
    return render (request, 'registration/signup.html', {})

def login (request):
    return render (request, 'registration/login.html', {})