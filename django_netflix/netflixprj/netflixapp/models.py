from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICE=(
    ('All','All'),
    ('Kids','Kids')
)

MOVIE_CHOICE=(
    ('Seasonal','Seasonal'),
    ('Single','Single')
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField("Profile", blank=True)

class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICE)
    uuid=models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title=models.CharField(max_length=225)
    description=models.TextField(blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4)
    type=models.CharField(max_length=10,choices=MOVIE_CHOICE)    
    videos=models.ManyToManyField('Video')
    flyer=models.ImageField(upload_to='flyers')
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICE)

    def __str__(self):
        return self.title
    


class Video(models.Model):
    title=models.CharField(max_length=225,null=True,blank=True)
    file=models.FileField(upload_to='movies')
    
    def __str__(self):
        return self.title
    
        

# Create your models here.
