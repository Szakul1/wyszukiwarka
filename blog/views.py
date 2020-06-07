from .models import University, Course
from blog.components.progressBar import create_progress
from blog.components.courseGraph import create_graph
from blog.components.button import create_checkbox, is_created
from .filters import CourseFilter, UniversityFilter
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def ulotka(request):
    """Widok startowy"""
    return render(request, 'blog/ulotka.html')




def comparison(request):
    """Zwraca widok dla wykresu z porownaniami"""
    is_created()
    return render(request, 'blog/comparison.html', None)


class UniversityListView(ListView):
    """Widok dla listy uniwersytetow"""
    model = University
    template_name = 'blog/university.html'
    context_object_name = 'universities'
    ordering = ['nazwa']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """Zwraca kontekst przy wywolywaniu template'a
        Filtruje wedlug wyszukiwarki"""
        context = super().get_context_data(**kwargs)
        context['filter'] = UniversityFilter(self.request.GET,
                                             queryset=self.get_queryset())
        return context


class UniversityDetailView(DetailView):
    """Widok dla uniwersytetu"""
    model = University


class CourseListView(ListView):
    """Widok dla listy kierunkow"""
    model = Course
    template_name = 'blog/course.html'
    context_object_name = 'courses'
    ordering = ['nazwa']
    paginate_by = 10

    def get_context_data(self, *args, object_list=None, **kwargs):
        """Zwraca kontekst przy wywolywaniu template'a
        Tworzy checkboxy dla kierunkow
        Filtruje wedlug wyszukiwarki"""
        objects = self.get_queryset().all()
        create_checkbox(objects)
        context = super().get_context_data(**kwargs)
        context['filter'] = CourseFilter(self.request.GET,
                                         queryset=self.get_queryset())
        return context


class CourseDetailView(DetailView):
    """Widok dla kierunku"""
    model = Course

    def get_context_data(self, **kwargs):
        """Zwraca kontekst przy wywolywaniu template'a
        Tworzy wykres i paski postepu
        """
        create_graph(self.get_object())
        create_progress(self.get_object())
        context = super().get_context_data(**kwargs)
        return context


class CourseCreateView(LoginRequiredMixin, CreateView):
    """Widok dla tworzenia kierunku"""
    model = Course
    fields = ['nazwa', 'uniwersytet', 'description',
              'tryb', 'tytul', 'grade', 'semesters',
              'department', 'm_to_w_ratio', 'international_ratio',
              'would_choose_again', 'avg_salary', 'function']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Widok dla zmieniania kierunku"""
    model = Course
    fields = ['nazwa', 'uniwersytet', 'description',
              'tryb', 'tytul', 'grade', 'semesters',
              'department', 'm_to_w_ratio', 'international_ratio',
              'would_choose_again', 'avg_salary', 'function']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Widok dla usuwania kierunku"""
    model = Course
    success_url = '/'

    def test_func(self):
        return True


class UniversityCreateView(LoginRequiredMixin, CreateView):
    """Widok dla tworzenia uniwersytetu"""
    model = University
    fields = ['nazwa', 'lokacja', 'typ',
              'national_ranking', 'website_url']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UniversityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Widok dla zmieniania uniwersytetu"""
    model = University
    fields = ['nazwa', 'lokacja', 'typ',
              'national_ranking', 'website_url']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True


class UniversityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Widok dla usuwania uniwersytetu"""
    model = University
    success_url = '/'

    def test_func(self):
        return True