from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from model_utils import Choices

# Create your models here.
AGE_CHOICES = Choices(
    (0, 'kids', 'kids'),
    (1, 'teens', 'teens'),
    (2, 'adults', 'adults'),
    )
# class AgeLimit(models.IntegerChoices):
#     Adult = 18
#     Young = 12
#     Children = 0
#
#
# agelimit = models.IntegerField(choices=AgeLimit.choices, null=True, blank=True)


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age_limit = models.IntegerField(choices=AGE_CHOICES, null=True, blank=True)


    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)

    class Meta:
        unique_together = ('name', 'surname')
    def __str__(self):
        return f'{self.name} {self.surname}'


class Country(models.Model):
    country = models.CharField(max_length=40, unique=True, null=True)

    class Meta:
        ordering = ['country']

    def __str__(self):
        return self.country


class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        null=True, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    category = models.CharField(null=True, max_length=100)
    released = models.DateField(null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)
    countries = models.ManyToManyField(Country, related_name='movies')
    # user = models.ForeignKey

    class Meta:
        unique_together = ('title', 'released')

    def __str__(self):
        return f"{self.title} from {self.released}"

