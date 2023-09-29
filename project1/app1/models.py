from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)
    image_path = models.ImageField(upload_to='category_images/',default = 'static/images/default.png')

    def __str__(self):
        return self.category
    




class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    Title= models.CharField(max_length=100)
    course_description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null = True)
    course_photo = models.ImageField(upload_to='course_photos/',default = 'static/images/default.png')
   

    def __str__(self):
        return self.Title







class UserAccount(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course,blank=True)
    registered_on = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]
    objects = CustomUserManager()


    def __str__(self):
        return self.email
    

class Difficultylevel(models.Model):
    level = models.CharField(max_length=200)

    def __str__(self):
        return self.level


class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    topic_content = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null = True)
    
    level = models.ForeignKey(Difficultylevel,on_delete= models.CASCADE,null = True)


    def __str__(self):
        return self.Title

    '''class Meta:
        ordering = ['order']'''#this can be used to define in which order the data can be retrived from the database


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
