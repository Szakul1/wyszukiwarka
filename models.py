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
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    
    types = [(1, 'stacjonarne'),
             (2, 'niestacjonarne')]
    
    types1 = [(1, 'licencjat'),
              (2, 'inzynier'),
              (3, 'magister')]
    
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    type_1 = models.CharField(max_length=100, choices=types)
    type_2 = models.CharField(max_length=100, choices=types1) 
    grade = models.IntegerField()
    semesters = models.IntegerField()
    department = models.CharField(max_length=100)
    m_to_w_ratio = models.IntegerField(default=55)
    international_ratio = models.IntegerField(default=55)
    would_choose_again = models.IntegerField(default=55)
    avg_salary = models.IntegerField(default=55)
    