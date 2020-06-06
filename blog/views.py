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
from .models import Post, University, Course
from blog.components.proggresBar import create_progress
from blog.components.courseGraph import create_graph
from blog.components.button import create_checkbox, is_created


def ulotka(request):
    
    return render(request, 'blog/ulotka.html')

def home(request):
    context = {
        'universities': University.objects.all(),
        'courses': Course.objects.all()
    }
    return render(request, 'blog/home.html', context)

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

      
