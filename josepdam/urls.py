from django.urls import path
from . import views 
from .views import HomeView, ArticleDetailView, TeamView, ArticleTeamDetailView, TeamDirectorView,BlogView,AboutView
from .views import ArticleBoardOfDirectorDetailView, BlogArticleDetailView,SecondConstructionDetailViewArticleDetailView


urlpatterns = [
    path('base/', views.base, name='base'),
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    path('article2/<int:pk>/', SecondConstructionDetailViewArticleDetailView.as_view(), name="second_detail"),
    path('about/', AboutView.as_view(), name='about'),
    path('our_services/', views.OurServices, name='our_services'),
    path('blog/', BlogView.as_view(), name="blog"),
    path('article_blog/<int:pk>/', BlogArticleDetailView.as_view(), name="detail-blog"),
    path('contact/', views.contact, name='contact'),
    path('video/', views.video, name='video'),
    path('our_projects/', views.OurProjects, name='our_projects'),
    path('message/', views.message, name='message'),
    path('team/', TeamView.as_view(), name='team'),
    path('article_team/<int:pk>/', ArticleTeamDetailView.as_view(), name="detail-team"),
    path('director/', TeamDirectorView.as_view(), name='director'),
    path('article_board_of_director/<int:pk>/', ArticleBoardOfDirectorDetailView.as_view(), name="detail-director"),
    #path('post/<int:post_id>/like/', views.like_post, name='post-detail'),
    path('article/<int:post_id>/like/', views.like_post, name='like-post'),

   

]