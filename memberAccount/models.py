from django.db import models
from django.contrib.auth.models import AbstractUser

class memberRegister(models.Model):
    username = models.CharField (max_length = 200)
    email = models.EmailField (max_length = 200, unique=True)
    password = models.CharField (max_length = 200)

    def __str__(self):
        return self.username
    

