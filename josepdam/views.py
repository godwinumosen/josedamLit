from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import ConstructionPost
from django.contrib import messages
from django.urls import reverse_lazy

def base (request):
    return render(request,"base.html")

'''def home (request):
    return render(request,"josep/home.html", {})'''

class HomeView(ListView):
    model = ConstructionPost
    template_name = 'josep/home.html'

class ArticleDetailView(DeleteView):
    model = ConstructionPost
    template_name = 'josep/article_detail.html'

    def ArticleDetailView(request, pk):  
        object = get_object_or_404(ConstructionPost, pk=pk)
        return render(request, 'article_detail.html', {'detail': object})




