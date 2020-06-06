# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from .views import (
        PostListView,
        PostDetailView,
        PostCreateView,
        PostUpdateView,
        PostDeleteView,
        ulotka,
)

from search import views as search_views

urlpatterns = [
    path('', ulotka, name='blog-home'),
    #path('home/', views.PostListView.as_view(), name='home'),
    path('search/', search_views.search, name='search'),
    #path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),        
    ]
