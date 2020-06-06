# -*- coding: utf-8 -*-
import django_filters
from django import forms
from django_filters import ChoiceFilter
from blog.models import Course, University

class CourseFilter(django_filters.FilterSet):
    
    CHOICES = (
            ('ascending', 'Ascending'),
            ('descending', 'Descending')
            )
    
    #ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')
    #name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Course
        fields = {'nazwa', 'uniwersytet', 'tryb', 'tytul'}
        
    def filter_by_order(self, queryset, name, value):
        expression = 'pub_date' if value == 'ascending' else '-pub_date'
        return queryset.order_by(expression)
    
class UniversityFilter(django_filters.FilterSet):
        
    
    CHOICES = (
            ('rosnaco', 'Rosnaco'),
            ('malejaco', 'Malejaco')
            )
    
    ordering = django_filters.ChoiceFilter(label='Ranking', choices=CHOICES, method='filter_by_order')
    #name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = University
        fields = {'nazwa', 'lokacja', 'typ'}
        
    def filter_by_order(self, queryset, name, value):
        expression = 'national_ranking' if value == 'rosnaco' else '-national_ranking'
        return queryset.order_by(expression)
    
        
        