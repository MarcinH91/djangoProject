from django.http import HttpResponse
from django import views
from django.shortcuts import render
from django.views.generic import ListView
from core.models import Movie
# Create your views here.

# class MovieView(ListView):
#     # template_name = 'movies.html'
#     # model = Movie
def movie(request):
    return render(
        request,
        template_name='movies.html',
        context={'movies': Movie.objects.all()}
    )

def hello(request):
    return render(
        request,
        template_name='hello.html',
        context={'adjectives': ['beautiful', 'cruel', 'wonderful']},
    )