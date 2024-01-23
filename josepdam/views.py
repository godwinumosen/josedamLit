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

#The main HomeView page
class HomeView(ListView):
    model = ConstructionPost
    template_name = 'josep/home.html'

#The ArticleDetailView page
class ArticleDetailView(DeleteView):
    model = ConstructionPost
    template_name = 'josep/article_detail.html'

    def ArticleDetailView(request, pk):  
        object = get_object_or_404(ConstructionPost, pk=pk)
        return render(request, 'article_detail.html', {'detail': object})
    
# The Contact
def contact (request):
    email='josepdam@gmail.com'
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']
        
        messages.success(request, f'Your email was sent Successfully we will get back to you {message_name}..!')
        return redirect('/home')
    else:
        context={
            'email':email
        }
        return render(request, 'josep/contact.html',context)

# The about page
def about (request):
    return render (request,'josep/about.html' )


#Whatsapp Messages
def whatsapp_message(request):
    whatsapp_number = '+2347016087680'
    whatsapp_link = f'https://api.whatsapp.com/send?phone={whatsapp_number}'
    context = {'whatsapp_link': whatsapp_link}
    return render(request, 'whatsapp_message.html', context)



