from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, default=title)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
class University(models.Model):
    
    types = [(1, 'Politechnika'),
             (2, 'Uniwersytet Ogólny'),
             (3, 'Uniwersytet Medyczny'),
             (4, 'Uniwersytet Ekonomiczny'),
             (5, 'Uniwersytet Przyrodniczy')]
    
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    type_1 = models.CharField(max_length=100, choices=types)
    national_ranking = models.IntegerField()
    website_url = models.URLField()