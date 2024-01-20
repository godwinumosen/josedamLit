from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class ConstructionPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField (max_length=255)
    img = models.ImageField ( upload_to= 'image/')
    publish_date = models.DateTimeField (auto_now_add= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-publish_date']
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse ('home')