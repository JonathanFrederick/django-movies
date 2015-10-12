from django.shortcuts import render
from django.db.models import Avg, Count
from .models import Movie, Rater

# Create your views here.


def top_20(request):
    movies = Movie.objects.annotate(num_ratings=Count('rating')) \
                                    .filter(num_ratings__gte=100) \
                                    .annotate(Avg('rating__stars')) \
                                    .order_by('-rating__stars__avg')[:20]

    return render(request,
                  'ratingsdb/top-20.html',
                  {'movies': movies})


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request,
                  'ratingsdb/show-movie.html',
                  {'movie': movie})


def rater_detail(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    return render(request,
                  'ratingsdb/show-rater.html',
                  {'rater': rater})
