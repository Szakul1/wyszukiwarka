from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class University(models.Model):
    types = (('politechnika', 'Politechnika'),
             ('uniwersytet ogolny', 'Uniwersytet Ogólny'),
             ('uniwersytet medyczny', 'Uniwersytet Medyczny'),
             ('uniwersytet ekonomiczny', 'Uniwersytet Ekonomiczny'),
             ('uniwersytet przyrodniczy', 'Uniwersytet Przyrodniczy'))

    nazwa = models.CharField(max_length=100)
    lokacja = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    typ = models.CharField(max_length=100, choices=types)
    national_ranking = models.IntegerField()
    website_url = models.URLField()

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Course(models.Model):
    types = (('stacjonarne', 'Stacjonarne'),
             ('niestacjonarne', 'Niestacjonarne'))

    types1 = (('licencjat', 'Licencjat'),
              ('inzynier', 'Inzynier'),
              ('magister', 'Magister'))

    nazwa = models.CharField(max_length=100)
    uniwersytet = models.ForeignKey(University, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    tryb = models.CharField(max_length=100, choices=types)
    tytul = models.CharField(max_length=100, choices=types1)
    grade = models.IntegerField()
    semesters = models.IntegerField()
    department = models.CharField(max_length=100)
    m_to_w_ratio = models.IntegerField(default=55)
    international_ratio = models.IntegerField(default=55)
    would_choose_again = models.IntegerField(default=55)
    avg_salary = models.IntegerField(default=55)
    function = models.IntegerField(default=55)

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
