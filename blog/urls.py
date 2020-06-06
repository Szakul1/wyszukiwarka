# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views
from .views import (
    UniversityListView,
    UniversityDetailView,
    CourseListView,
    CourseDetailView,
    comparison,
    ulotka,
)

urlpatterns = [
    path('', ulotka, name='blog-home'),

    path('univerisities', UniversityListView.as_view(),
         name='blog-universities'),
    path('univerisities/<int:pk>', UniversityDetailView.as_view(),
         name='university-detail'),
    path('courses', CourseListView.as_view(), name='blog-courses'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course-detail'),

    path('comparison', comparison, name='blog-comparison'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]
