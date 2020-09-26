import logging

from django.http import HttpResponse
from django import views
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView, DetailView
from core.models import Movie, AGE_CHOICES
from core.forms import MovieForm

logging.basicConfig(filename='log.txt',
                    filemode='w',
                    level=logging.INFO,)
LOGGER = logging.getLogger(__name__)
# Create your views here.
class MovieCreateView(CreateView):
    title = 'Add Movie'
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)
## w Pythonie 3.8 pójdzie to rozwiązanie(walrus operator - :=):
    # def post(self, request, *args, **kwargs):
    #     result = super().post(request, *args, **kwargs)
    #     if title := request._post.get('title'):
    #         LOGGER.info(f'Successfully added new movie: {title}')
    #     return result
    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        title = request.POST.get('title')
        if title:
            LOGGER.info(f"Successfully added new movie: {self.request.POST.get('title')}")
        return result
class MovieListView(ListView):
    template_name = 'movie_list.html'
    model = Movie

class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie


class MovieUpdateView(UpdateView):
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

class MovieDeleteView(DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')




# class MovieView(ListView):
#     template_name = 'movies.html'
#     model = Movie
    # extra_context = {'movies': Movie.objects.all(), 'limits': AGE_CHOICES}

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=None, **kwargs)
    #     context['limits'] = AGE_CHOICES
    #     return context








# def movie(request):
#     return render(
#         request,
#         template_name='movies.html',
#         context={'movies': Movie.objects.all(), 'limits': AGE_CHOICES}
#     )

def hello(request):
    LOGGER.info('\nWreszcie coś działa.')
    return render(
        request,
        template_name='hello.html',
        context={'adjectives': ['beautiful', 'cruel', 'wonderful']},
    )


