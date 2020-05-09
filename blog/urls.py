# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from .views import (
    UniversityListView,
    UniversityDetailView,
    CourseListView,
    CourseDetailView,
    PostListView,
    UserPostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),

    path('univerisities', UniversityListView.as_view(), name='blog-universities'),
    path('univerisities/<int:pk>', UniversityDetailView.as_view(), name='university-detail'),
    path('courses', CourseListView.as_view(), name='blog-courses'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course-detail'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
