from django.db import models
from django.contrib.auth.models import User

# from .models import Profile
from .forms import UserForm

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
