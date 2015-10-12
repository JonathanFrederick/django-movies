from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login

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
