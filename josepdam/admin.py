from django.contrib import admin
# Register your models here.
from . import models
from .models import ConstructionPost,SecondConstruction,TeamsPost, Board_Of_DirectorPost, BlogPost

#The Construction post model admin of josepdam
class ConstructionPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title','description','author','img']
admin.site.register(ConstructionPost, ConstructionPostModelAdmin)


#SecondConstruction post
class SecondConstructiontModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title','description','author','image1']
admin.site.register(SecondConstruction, SecondConstructiontModelAdmin)


#The blog post model admin of josepdam
class BlogPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title','description','author','img']
admin.site.register(BlogPost, BlogPostModelAdmin)

class TeamsModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('worker_name',)}
    list_display = ['worker_name','worker_position','worker_description']
admin.site.register(TeamsPost, TeamsModelAdmin ) 

#board of directors in josepdam
class Board_Of_Director_ModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('board_of_director_name',)}
    list_display = ['board_of_director_name','board_of_director_position','board_of_director_description']
admin.site.register(Board_Of_DirectorPost, Board_Of_Director_ModelAdmin)



