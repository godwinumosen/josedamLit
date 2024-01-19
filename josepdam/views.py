from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy

def base (request):
    return render(request,"base.html")

def index (request):
    return render(request,"josep/index.html")
