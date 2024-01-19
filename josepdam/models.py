from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Construction(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField (max_length=200)
    img = models.ImageField ( upload_to= 'image/')
    publish_date = models.DateTimeField (auto_now_add= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-publish_date']
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)