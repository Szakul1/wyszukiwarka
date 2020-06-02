# -*- coding: utf-8 -*-
import django_filters

from blog.models import Post

class PostFilter(django_filters.FilterSet):
    
    CHOICES = (
            ('ascending', 'Ascending'),
            ('descending', 'Descending')
            )
    
    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')
    
    class Meta:
        model = Post
        fields = {'title'}
        
    def filter_by_order(self, queryset, name, value):
        expression = 'pub_date' if value == 'ascending' else '-pub_date'
        return queryset.order_by(expression)
        
        
        