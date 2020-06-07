# -*- coding: utf-8 -*-
import django_filters
from django import forms
from django_filters import ChoiceFilter
from blog.models import Course, University

"""Fiter uzywany przy wyszukiwaniu modelu"""
class CourseFilter(django_filters.FilterSet):
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )
    uniwersytet = django_filters.ModelMultipleChoiceFilter(
        queryset=University.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label="Foo")

    class Meta:
        model = Course
        fields = {'nazwa', 'tryb', 'tytul'}

    def filter_by_order(self, queryset, name, value):
        expression = 'pub_date' if value == 'ascending' else '-pub_date'
        return queryset.order_by(expression)

"""Fiter uzywany przy wyszukiwaniu modelu"""
class UniversityFilter(django_filters.FilterSet):
    """mozliwe opcje przy filtrowaniu wzgledem kolejnosci"""
    CHOICES = (
        ('rosnaco', 'Rosnaco'),
        ('malejaco', 'Malejaco')
    )

    """pole obrazujace kolejnosc wzgledem miejsca w rankingu"""
    ordering = django_filters.ChoiceFilter(label='Ranking', choices=CHOICES,
                                           method='filter_by_order')

    class Meta:
        model = University
        fields = {'nazwa', 'lokacja', 'typ'}

    def filter_by_order(self, queryset, name, value):
        expression = 'national_ranking' if value == 'rosnaco' else '-national_ranking'
        return queryset.order_by(expression)
