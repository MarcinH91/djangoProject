from core.views import MovieListView


class IndexView(MovieListView):
    title = 'Welcome to Django Movies!'
    template_name = 'index.html'