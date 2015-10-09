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
            new_user = form.save()
            password = new_user.password

            new_user.set_password(password)
            new_user.save()

            Rater(user=new_user).save()

            new_user = authenticate(username=new_user.username,
                                    password=password)

            login(request, new_user)
            return redirect('top_20')

    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})
