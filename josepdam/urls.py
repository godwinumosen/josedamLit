from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, TeamView, ArticleTeamDetailView, TeamDirectorView
from .views import ArticleBoardOfDirectorDetailView


urlpatterns = [
    path('base/', views.base, name='base'),
   # path ('', views.home, name='home'),
   path('', HomeView.as_view(), name="home"),
   path('home/', HomeView.as_view(), name='home'),
   path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('message/', views.message, name='message'),
   
   path('team/', TeamView.as_view(), name='team'),
   path('article_team/<int:pk>/', ArticleTeamDetailView.as_view(), name="detail-team"),
   path('director/', TeamDirectorView.as_view(), name='director'),
   path('article_board_of_director/<int:pk>/', ArticleBoardOfDirectorDetailView.as_view(), name="detail-director"),

]