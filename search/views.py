from django.shortcuts import render
from blog.models import Course, Post
import json
from django.http import HttpResponse
from django.views.generic import ListView

from .filters import CourseFilter

#from .documents import PostDocument
# Create your views here.

def main_search(request):
    
    return render(request, 'search/main_search.html')

def search(request):
    
    #posts = Post.objects.all()
    posts = {'value': 111}
        
    return render(request, 'search/search_autocomplete.html', {'posts': posts})

def auto_complete(request):
    
    
    query = request.GET.get("term", "")
    posts = Post.objects.filter(title__icontains=query)
    #posts = Post.objects.all()
    
    results = []
    
    for post in posts:
        place_json = post.title
        results.append(place_json)
    
    data = json.dumps(results)
    
    return HttpResponse(data)
    
class CourseListView(ListView):
    
    model = Course
    template_name = 'blog/home.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CourseFilter(self.request.GET, queryset=self.get_queryset())
        return context