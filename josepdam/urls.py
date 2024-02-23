from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, TeamView, ArticleTeamDetailView, TeamDirectorView,BlogView
from .views import ArticleBoardOfDirectorDetailView, BlogArticleDetailView


urlpatterns = [
    path('base/', views.base, name='base'),
    # path ('', views.home, name='home'),
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    path('about/', views.about, name='about'),
    #path('blog/', views.blog, name='blog'),
    path('blog/', BlogView.as_view(), name="blog"),
    path('article_blog/<int:pk>/', BlogArticleDetailView.as_view(), name="detail-blog"),
    path('contact/', views.contact, name='contact'),
    path('message/', views.message, name='message'),
    path('team/', TeamView.as_view(), name='team'),
    path('article_team/<int:pk>/', ArticleTeamDetailView.as_view(), name="detail-team"),
    path('director/', TeamDirectorView.as_view(), name='director'),
    path('article_board_of_director/<int:pk>/', ArticleBoardOfDirectorDetailView.as_view(), name="detail-director"),
    #path('post/<int:post_id>/like/', views.like_post, name='post-detail'),
    path('article/<int:post_id>/like/', views.like_post, name='like-post'),
    path('location/', views.location, name='location'),
   

]