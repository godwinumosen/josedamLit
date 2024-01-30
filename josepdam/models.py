from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class ConstructionPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField (max_length=255)
    img = models.ImageField ( upload_to= 'image/')
    publish_date1 = models.DateTimeField (auto_now_add= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    location = models.CharField(max_length = 2200)

    class Meta:
        ordering =['-publish_date1']
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse ('home')
    

class TeamsPost (models.Model):
    worker_name = models.CharField (max_length = 200)
    worker_position = models.CharField (max_length = 200)
    worker_description = models.TextField()
    worker_img = models.ImageField(upload_to='images')
    slug = models.SlugField (max_length=25)
    publish_date = models.DateTimeField (auto_now_add= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-publish_date']

    def get_absolute_url(self):
        return reverse ('home')
    
    def __str__(self):
        return self.worker_name + ' | ' + str(self.author)