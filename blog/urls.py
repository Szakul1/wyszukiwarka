# -*- coding: utf-8 -*-
"""Tablica ze sciezkami w projekcie"""
from django.urls import path, include
from .views import (
    UniversityListView,
    UniversityDetailView,
    CourseListView,
    CourseDetailView,
    comparison,
    ulotka,

    CourseCreateView,
    CourseDeleteView,
    CourseUpdateView,
    UniversityCreateView,
    UniversityDeleteView,
    UniversityUpdateView,
)

urlpatterns = [
    path('', ulotka, name='blog-home'),

    path('universities', UniversityListView.as_view(),
         name='blog-universities'),
    path('universities/<int:pk>', UniversityDetailView.as_view(),
         name='university-detail'),
    path('courses', CourseListView.as_view(), name='blog-courses'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course-detail'),

    path('comparison', comparison, name='blog-comparison'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),

    path('courses/new/', CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(),
         name='course-update'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(),
         name='course-delete'),

    path('universities/new/', UniversityCreateView.as_view(),
         name='university-create'),
    path('universities/<int:pk>/update/', UniversityUpdateView.as_view(),
         name='university-update'),
    path('universities/<int:pk>/delete/', UniversityDeleteView.as_view(),
         name='university-delete'),
]
