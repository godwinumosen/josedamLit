from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

#The search button model of locatin
    
# The main Josepdam Model
class ConstructionPost(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    slug = models.SlugField (max_length=255)
    img = models.ImageField ( upload_to= 'image/')
    publish_date = models.DateTimeField (auto_now_add= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    rent = models.IntegerField()
    size = models.IntegerField()
    details = models.CharField(max_length = 200,blank=True, null=True)
    location = models.CharField(max_length = 200,blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    
    class Meta:
        ordering =['-publish_date']
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse ('home')
    
#The second main Josepdam Model
class SecondConstruction(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    slug = models.SlugField (max_length=255)
    image1 = models.ImageField ( upload_to= 'image2/')
    publish_date = models.DateTimeField (auto_now_add= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.IntegerField()
    details = models.CharField(max_length = 200,blank=True, null=True)
    location = models.CharField(max_length = 200,blank=True, null=True)
    
    class Meta:
        ordering =['-publish_date']
    
    def __str__(self):
        return self.title+ ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse ('home')

    

# The like and unlike model for each property
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(ConstructionPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
# The Josepdam team Model
class TeamsPost (models.Model):
    worker_name = models.CharField (max_length = 200, blank=True, null=True)
    worker_position = models.CharField (max_length = 200, blank=True, null=True)
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
    
# The josepdam board of director Model
class Board_Of_DirectorPost (models.Model):
    board_of_director_name = models.CharField (max_length = 200, blank=True, null=True)
    board_of_director_position = models.CharField (max_length = 210, blank=True, null=True)
    board_of_director_description = models.TextField()
    board_of_director_img = models.ImageField(upload_to='images_dir')
    slug = models.SlugField (max_length=25)
    publish_date = models.DateTimeField (auto_now_add= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-publish_date']

    def get_absolute_url(self):
        return reverse ('home')
    
    def __str__(self):
        return self.board_of_director_name + ' | ' + str(self.author)
    

# The blog post of Josepdam Model
class BlogPost(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    slug = models.SlugField (max_length=255)
    img = models.ImageField ( upload_to= 'image_blog/')
    publish_date = models.DateTimeField (auto_now_add= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    location = models.CharField(max_length = 200,blank=True, null=True)
    
    

    class Meta:
        ordering =['-publish_date']
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse ('home')