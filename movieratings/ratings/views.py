from django.shortcuts import render
from .models import Movie

# Create your views here.


def top_20(request):
    movies = sorted([m for m in Movie.objects.all()
                    if type(m.average_rating()) == float],
                    key=lambda r: r.average_rating(),
                    reverse=True)[:20]
    return render(request,
                  'ratings/top-20-movies.html',
                  {'top': movies})
