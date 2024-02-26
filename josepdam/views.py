from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import ConstructionPost, TeamsPost, Board_Of_DirectorPost, Like, BlogPost
from django.contrib import messages
from django.http import HttpResponse
import folium
import geocoder
from django.urls import reverse
from django.urls import reverse_lazy


def base (request):
    return render(request,"base.html")

'''def home (request):
    return render(request,"josep/home.html", {})'''

#The main HomeView page
class HomeView(ListView):
    model = ConstructionPost
    template_name = 'josep/home.html'

class BlogView(ListView):
    model = BlogPost
    template_name = 'josep/blog.html'

#The ArticleDetailView page
class ArticleDetailView(DetailView):
    model = ConstructionPost
    template_name = 'josep/article_detail.html'

    def ArticleDetailView(request, pk):  
        object = get_object_or_404(ConstructionPost, pk=pk)
        return render(request, 'article_detail.html', {'detail': object})

def blog (request):

    return render (request, 'josep/blog.html', {})   

# The Contact view been implemented
def contact (request):
    email='josepdam@gmail.com'
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']
        
        messages.success(request, f'Your email was sent Successfully {message_name}..!')
        return redirect('/message')
    else:
        context={
            'email':email
        }
        return render(request, 'josep/contact.html',context)

def message (request):
    return render (request, 'josep/message.html', {})

# The about page
def about (request):
    return render (request,'josep/about.html' )


#Whatsapp Messages
def whatsapp_message(request):
    whatsapp_number = '+2348066295770'
    whatsapp_link = f'https://api.whatsapp.com/send?phone={whatsapp_number}'
    context = {'whatsapp_link': whatsapp_link}
    return render(request, 'whatsapp_message.html', context)

#The Team class base
class TeamView (ListView):
    model = TeamsPost
    template_name = 'josep/team.html'

#The Team article details
class ArticleTeamDetailView(DetailView):
    model = TeamsPost
    template_name = 'josep/article_team_detail.html'

    def ArticleTeamDetailView(request, pk):  
        object = get_object_or_404(TeamsPost, pk=pk)
        return render(request, 'article_team_detail.html', {'detail': object})


#The Directors Team class base
class TeamDirectorView (ListView):
    model = Board_Of_DirectorPost
    template_name = 'josep/board_of__director.html'
    
#the desplay details for director
class ArticleBoardOfDirectorDetailView(DetailView):
    model = Board_Of_DirectorPost
    template_name = 'josep/article_board_of_director.html'

    def ArticleBoardOfDirectorDetailView(request, pk):  
        object = get_object_or_404(Board_Of_DirectorPost, pk=pk)
        return render(request, 'article_board_of_director.html', {'detail': object})
    
#the desplay details for blog post
class BlogArticleDetailView(DetailView):
    model = BlogPost
    template_name = 'josep/blog_article_detail.html'

    def BlogArticleDetailView(request, pk):  
        object = get_object_or_404(Board_Of_DirectorPost, pk=pk)
        return render(request, 'blog_article_detail.html', {'detail': object})

#The like view of the details page
def like_post(request, post_id):
    post = ConstructionPost.objects.get(pk=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    # Redirect the user to the same page or a different page
    return redirect(reverse('like-post', kwargs={'post_id': post_id}))
    

#The like view of the details page
def like_post(request, post_id):
    post = get_object_or_404(ConstructionPost, pk=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    # Redirect the user back to the article detail page
    return redirect(reverse('detail', kwargs={'pk': post_id}))

# Map location from the database system
'''def location(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    #address = 'Lekki Lagos Nigeria'
    locations1 = geocoder.osm(address)
    lat =locations1.lat
    lng =locations1.lng
    country =locations1.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Your address have to be country or state..')
    locations = folium.Map(map_location=[19, 12], zoom_start=600)
    folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(locations)
    locations=locations._repr_html_()
    context = {
        'locations':locations,
        'form':form,
    }
    return render(request, 'josep/location.html', context)'''
