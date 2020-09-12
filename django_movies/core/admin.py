from django.contrib import admin

# Register your models here.
from core.models import Movie, Genre, Director, Country
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Country)


