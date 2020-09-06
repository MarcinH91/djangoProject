from django.contrib import admin

# Register your models here.
from core.models import Movie, Genre, Director
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Director)
