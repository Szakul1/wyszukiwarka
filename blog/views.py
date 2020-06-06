from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
)
from .models import University, Course, Post
from .components.proggresBar import create_progress
from .components.courseGraph import create_graph
from .components.button import create_checkbox, is_created


def ulotka(request):
    
    return render(request, 'blog/ulotka.html')

def home(request):
    context = {
        'universities': University.objects.all(),
        'courses': Course.objects.all()
    }
    return render(request, 'blog/home.html', context)

def comparison(request):
    is_created()
    return render(request, 'blog/comparison.html', None)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-pub_date']
    paginate_by = 2

'''
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2
    
    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-pub_date')
'''       

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    
class UniversityListView(ListView):
    model = University
    template_name = 'blog/university.html'
    context_object_name = 'universities'
    ordering = ['name']
    paginate_by = 10


class UniversityDetailView(DetailView):
    model = University


class CourseListView(ListView):
    model = Course
    template_name = 'blog/course.html'
    context_object_name = 'courses'
    ordering = ['name']
    paginate_by = 10

    def get_context_data(self, *args, object_list=None, **kwargs):
        objects = self.get_queryset().all()
        create_checkbox(objects)
        context = super().get_context_data(**kwargs)
        return context


class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        create_graph(self.get_object())
        create_progress(self.get_object())
        context = super().get_context_data(**kwargs)
        return context
