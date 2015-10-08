from django.shortcuts import render
from .models import Movie, Rater

# Create your views here.


def top_20(request):
    movies = sorted([m for m in Movie.objects.all()
                    if type(m.average_rating()) == float],
                    key=lambda r: r.average_rating(),
                    reverse=True)[:20]
    return render(request,
                  'ratings/top-20-movies.html',
                  {'top': movies})


def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    # ratings = movie.rating_set.all()
    return render(request,
                  'ratings/show-movie.html',
                  {'movie': movie})


def show_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    return render(request,
                  'ratings/show-rater.html',
                  {'rater': rater})
