# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views
from .views import (
        UniversityListView,
        UniversityDetailView,
        CourseListView,
        CourseDetailView,
        PostDetailView,
        PostCreateView,
        PostUpdateView,
        PostDeleteView,
        ulotka,
        comparison,
)

from search import views as search_views

urlpatterns = [
    path('', ulotka, name='blog-home'),
    #path('home/', views.PostListView.as_view(), name='home'),
    #path('search/', search_views.search, name='search'),
    #path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('universities/', UniversityListView.as_view(), name='blog-universities'),
    path('universities/<int:pk>/', UniversityDetailView.as_view(), name='university-detail'),
    path('courses/', CourseListView.as_view(), name='blog-courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('comparison', comparison, name='blog-comparison'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    ]
