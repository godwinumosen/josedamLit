from django.contrib import admin
# Register your models here.
from . import models
from .models import ConstructionPost, TeamsPost, Board_Of_DirectorPost

class ConstructionPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title','description','author','img']
admin.site.register(ConstructionPost, ConstructionPostModelAdmin)

class TeamsModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('worker_name',)}
    list_display = ['worker_name','worker_position','worker_description']
admin.site.register(TeamsPost, TeamsModelAdmin ) 

#board of directors in josepdam
class Board_Of_Director_ModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('board_of_director_name',)}
    list_display = ['board_of_director_name','board_of_director_position','board_of_director_description']
admin.site.register(Board_Of_DirectorPost, Board_Of_Director_ModelAdmin)