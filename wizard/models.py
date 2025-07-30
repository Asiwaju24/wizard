from django.db import models
from django.utils import timezone
import ckeditor_uploader
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
    
class Team(models.Model):
    name = models.CharField(max_length= 260, null=False, blank=False)
    image = models.ImageField(upload_to='team_image/')
    position = models.CharField(max_length=100, null=False, blank=False)
    linkedin = models.URLField(max_length=200)
    x = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.name
    

class Projects(models.Model):
    image = models.ImageField(upload_to='project/')

class Blog(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='blog_image/')
    body = RichTextUploadingField()
    tag = models.CharField(max_length=50, blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

class Language(models.Model):
    language = models.CharField(max_length=750)
    body = RichTextUploadingField()
    youtube_id = models.CharField(max_length=20000)
    
    def __str__(self):
        return self.language



class Field(models.Model):
    field = models.CharField(max_length=750)
    body = RichTextUploadingField()
    youtube_id = models.CharField(max_length=20000)

    def __str__(self):
        return self.field


class Feedback(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='customer/')
    feedback = RichTextUploadingField(max_length= 700)



class Inquiry(models.Model):
    full_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    project_type = models.CharField(max_length=100, blank=True, null=True)
    budget = models.CharField(max_length=100, blank=True, null=True)
    timeline = models.CharField(max_length=100, blank=True, null=True)
    message = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.project_type}"
