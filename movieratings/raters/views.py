from django.shortcuts import render, redirect
from .forms import UserForm, RateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.


def rater_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = user.password
            user.set_password(password)
            user.save()

            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            return redirect('top_20')
    else:
        form = UserForm()
    return render(request, 'raters/registration.html',
                  {'form': form})


@login_required
def user_rate(request):
    if request.method == 'POST':
        form = RateForm(request.POST)

        if form.is_valid():
            rating = form.save()
            rating.save()

            return redirect('db/movies/'+str(rating.movie))
    else:
        form = RateForm()
    return render(request, 'ratingsdb/show-movie.html',
                  {'form': form})
