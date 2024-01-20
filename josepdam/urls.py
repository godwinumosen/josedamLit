from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView


urlpatterns = [
    path('base/', views.base, name='base'),
   # path ('', views.home, name='home'),
   path('', HomeView.as_view(), name="home"),
   path('home/', HomeView.as_view(), name='home'),
   path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail")

]