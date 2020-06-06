from django.shortcuts import render
from blog.models import Course
import json
from django.http import HttpResponse
from django.views.generic import ListView

from .filters import CourseFilter


# from .documents import PostDocument
# Create your views here.

def main_search(request):
    return render(request, 'search/main_search.html')


def search(request):
    # posts = Post.objects.all()
    posts = {'value': 111}

    return render(request, 'search/search_autocomplete.html', {'posts': posts})


class CourseListView(ListView):
    model = Course
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CourseFilter(self.request.GET,
                                         queryset=self.get_queryset())
        return context
