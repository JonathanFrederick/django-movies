from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=215)


# class Rating(models.Model):
    # stars = models.PositiveSmallIntegerField()
    # rater = models.ForeignKey(Rater)
    # movie = models.ForeignKey(Movie)


class Rater(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    NOT_GIVEN = 'X'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NOT_GIVEN, 'X'),)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              null=True)
    zipcode = models.CharField(max_length=5, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    occupation = models.PositiveSmallIntegerField(null=True)
    user = models.OneToOneField(User, null=True)

    gender = models.CharField(max_length=1)
