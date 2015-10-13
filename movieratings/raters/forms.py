from django import forms
from django.contrib.auth.models import User
from ratingsdb.models import Rating


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('stars',)
