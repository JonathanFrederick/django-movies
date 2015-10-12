from django.db import models
from django.contrib.auth.models import User
import csv
import json
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=215)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']



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


class Rating(models.Model):
    stars = models.PositiveSmallIntegerField()
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)


def load_movies():
    movies = []
    with open('ratingsdb/data/movies.dat', encoding='windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames=['movie_id', 'title', 'genres'],
                                delimiter='\t')
        for line in reader:
            movie = {
                'fields': {
                    'title': line['title']
                },
                'model': 'ratingsdb.Movie',
                'pk': int(line['movie_id'])
            }
            movies.append(movie)

    with open('ratingsdb/fixtures/movies.json', 'w') as f:
        f.write(json.dumps(movies))


def load_raters():
    from faker import Faker
    import random

    fake = Faker()
    raters = []
    with open('ratingsdb/data/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames=['UserID', 'Gender', 'Age',
                                            'Occupation', 'Zip-code'],
                                delimiter='\t')
        for line in reader:
            User.objects.create_user(username=fake.user_name() +
                                     str(random.randint(100, 999)),
                                     email=fake.email(),
                                     password='password',
                                     pk=int(line['UserID']))
            rater = {
                'fields': {
                    'gender': line['Gender'],
                    'age': line['Age'],
                    'occupation': line['Occupation'],
                    'zipcode': line['Zip-code']
                },
                'model': 'ratingsdb.Rater',
                'pk': int(line['UserID'])
            }
            raters.append(rater)

    with open('ratingsdb/fixtures/raters.json', 'w') as f:
        f.write(json.dumps(raters))


def load_ratings():
    ratings = []
    with open('ratingsdb/data/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames=['UserID', 'MovieID',
                                            'Rating', 'Timestamp'],
                                delimiter='\t')
        for line in reader:
            rating = {
                'fields': {
                    'rater': line['UserID'],
                    'movie': line['MovieID'],
                    'stars': line['Rating']
                },
                'model': 'ratingsdb.Rating'
            }
            ratings.append(rating)

    with open('ratingsdb/fixtures/ratings.json', 'w') as f:
        f.write(json.dumps(ratings))


def load_data():
    load_raters()
    load_movies()
    load_ratings()
