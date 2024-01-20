from django.contrib import admin
# Register your models here.
from . import models
from .models import ConstructionPost

class ConstructionPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title','description','author','img']
admin.site.register(ConstructionPost, ConstructionPostModelAdmin)