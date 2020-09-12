from django.http import HttpResponse
from django import views
from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Movie, AGE_CHOICES

# Create your views here.

class MovieView(TemplateView):
    template_name = 'movies.html'
    extra_context = {'movies': Movie.objects.all(), 'limits': AGE_CHOICES}






# def movie(request):
#     return render(
#         request,
#         template_name='movies.html',
#         context={'movies': Movie.objects.all(), 'limits': AGE_CHOICES}
#     )

def hello(request):
    return render(
        request,
        template_name='hello.html',
        context={'adjectives': ['beautiful', 'cruel', 'wonderful']},
    )


