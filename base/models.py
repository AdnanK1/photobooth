from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    photo = CloudinaryField('photo')
    bio = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.bio

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=150)
    caption = models.TextField(null=True,blank=True)
    profile = models.ForeignKey(Profile,on_delete=models.SET_NULL, null=True)
    comments = models.TextField(null=True,blank=True)
    likes = models.ManyToManyField(User,blank=True,related_name='likes')
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name
    
    def number_of_likes(self):
        return self.likes.count()