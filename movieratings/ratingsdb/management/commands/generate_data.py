import csv
import json

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        load_data()


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
    from datetime import date
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
                    'stars': line['Rating'],
                    'timestamp': str(date.fromtimestamp(int(line['Timestamp'])))
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
