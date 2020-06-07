from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)
from .models import University, Course
from blog.components.progressBar import create_progress
from blog.components.courseGraph import create_graph
from blog.components.button import create_checkbox, is_created
from .filters import CourseFilter, UniversityFilter
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


class UniversityListView(ListView):
    model = University
    template_name = 'blog/university.html'
    context_object_name = 'universities'
    ordering = ['nazwa']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = UniversityFilter(self.request.GET,
                                             queryset=self.get_queryset())
        return context


class UniversityDetailView(DetailView):
    model = University


class CourseListView(ListView):
    model = Course
    template_name = 'blog/course.html'
    context_object_name = 'courses'
    ordering = ['nazwa']
    paginate_by = 10

    def get_context_data(self, *args, object_list=None, **kwargs):
        objects = self.get_queryset().all()
        create_checkbox(objects)
        context = super().get_context_data(**kwargs)
        context['filter'] = CourseFilter(self.request.GET,
                                         queryset=self.get_queryset())
        return context


class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        create_graph(self.get_object())
        create_progress(self.get_object())
        context = super().get_context_data(**kwargs)
        return context


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['nazwa', 'uniwersytet', 'description',
              'tryb', 'tytul', 'grade', 'semesters',
              'department', 'm_to_w_ratio', 'international_ratio',
              'would_choose_again', 'avg_salary', 'function']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    fields = ['nazwa', 'uniwersytet', 'description',
              'tryb', 'tytul', 'grade', 'semesters',
              'department', 'm_to_w_ratio', 'international_ratio',
              'would_choose_again', 'avg_salary', 'function']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return True


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    success_url = '/'

    def test_func(self):
        course = self.get_object()
        return True

class UniversityCreateView(LoginRequiredMixin, CreateView):
    model = University
    fields = ['nazwa', 'lokacja', 'typ',
              'national_ranking', 'website_url']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UniversityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = University
    fields = ['nazwa', 'lokacja', 'typ',
              'national_ranking', 'website_url']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return True


class UniversityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = University
    success_url = '/'

    def test_func(self):
        course = self.get_object()
        return True