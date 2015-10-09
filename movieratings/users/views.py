from django.shortcuts import render, redirect
from ratings.models import Rater
from .forms import UserForm
from django.contrib.auth import authenticate, login
from ratings import urls


# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = user.password

            user.set_password(password)
            user.save()

            profile = Profile(
                user=user,
            )
            profile.save()

            user = authenticate(username=user.username,
                                password=password)

            login(request, user)
            return redirect('top_20')

        else:
            form = UserForm()
        return render(request, 'users/register.html', {'form': form})
