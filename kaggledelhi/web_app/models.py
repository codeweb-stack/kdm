from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Speaker(models.Model):
    name=models.CharField(max_length=50)
    talk=models.CharField(max_length=100)
    about=models.CharField(max_length=500)
    image=models.ImageField(upload_to='images/')
    Linkedin=models.TextField()
    kaggle=models.TextField()
    github=models.TextField()
    slide=models.TextField()
    Notebook=models.TextField()
    code=models.TextField()
    pub_date=models.DateTimeField('date published',default=timezone.now)

class Program(models.Model):
    talk_time=models.CharField(max_length=10)
    talk=models.CharField(max_length=100)
    speaker=models.CharField(max_length=100)

class sponsors(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/')
    sponsorlink=models.TextField()


class pastspeakers(models.Model):
    name=models.CharField(max_length=50)
    talk=models.CharField(max_length=100)
    about=models.CharField(max_length=500)
    images=models.ImageField(upload_to='images/')
    Linkedin=models.TextField()
    kaggle=models.TextField()
    github=models.TextField()
    slide=models.TextField()
    Notebook=models.TextField()
    code=models.TextField()
    pub_date=models.DateTimeField('date published',default=timezone.now)


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
 
class post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title