from django.contrib import admin
# Register your models here.
from . import models
from .models import ConstructionPost, Teams

class ConstructionPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title','description','author','img']
admin.site.register(ConstructionPost, ConstructionPostModelAdmin)

class TeamsModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('worker_name',)}
    list_display = ['worker_name','worker_position','worker_description']
admin.site.register(Teams, TeamsModelAdmin ) 