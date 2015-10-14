from django.shortcuts import render, redirect
from .forms import UserForm, RateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from ratingsdb.views import Movie, Rater


# Create your views here.


def rater_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = user.password
            user.set_password(password)
            user.save()
            rater = Rater(user=user)
            rater.save()

            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            return redirect('top_20')
    else:
        form = UserForm()
    return render(request, 'raters/registration.html',
                  {'form': form})


@login_required
def user_rate(request, movie_id):
    from datetime import datetime

    if request.method == 'POST':
        form = RateForm(request.POST)

        if form.is_valid():
            rating = form.save(commit=False)
            rating.movie = Movie.objects.get(pk=movie_id)
            rating.rater = request.user.rater
            rating.timestamp = datetime.now()
            rating.save()

            return redirect('ratingsdb.views.movie_detail', movie_id=movie_id)
    else:
        form = RateForm()
    return render(request, 'ratingsdb/show-movie.html',
                  {'form': form, 'movie': movie_id})
