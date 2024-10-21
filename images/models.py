from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=200, unique=True)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    authors = models.ManyToManyField(User, related_name='authors')
    publication_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=500, default='')
    def __str__(self):
        return self.name
    
    def containstag(self, tag):
        return tag in self.tags.split()
    
    
class Rectangle(models.Model):
    picture = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='rectangles')
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    color = models.CharField(max_length=100)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    