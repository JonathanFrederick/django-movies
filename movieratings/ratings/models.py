from django.db import models


# Create your models here.
class Rater(models.Model):
    def __str__(self):
        return str(self.id)


class Movie(models.Model):
    title = models.CharField(max_length=215)

    def average_rating(self):
        # give key because aggregate returns as database entry
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']

    def __str__(self):
        return str(self.id) + ' - ' + str(self.title)


class Rating(models.Model):
    stars = models.SmallIntegerField()  # change to PositiveSmallIntegerField
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return '{}: {} ({})'.format(str(self.movie),
                                    str(self.stars),
                                    str(self.rater))


def load_initial_data():
    import csv
    import json

    raters = []
    with open('data/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='\t')
        for row in reader:
            rater = {
                'fields': {
                    #'gender': row['Gender'],
                    #'age': row['Age'],
                    #'occupation': row['Occupation'],
                    #'zipcode': row['Zip-code'],
                },
                'model': 'ratings.Rater',
                'pk': int(row['UserID']),
            }
            raters.append(rater)
    with open('ratings/fixtures/raters.json', 'w') as f:
        f.write(json.dumps(raters))

    movies = []
    with open('data/movies.dat', encoding='windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genres'
                                .split('::'),
                                delimiter='\t')
        for row in reader:
            movie = {
                'fields': {
                    'title': row['Title'],
                },
                'model': 'ratings.Movie',
                'pk': int(row['MovieID'])
            }
            movies.append(movie)

    with open('ratings/fixtures/movies.json', 'w') as f:
        f.write(json.dumps(movies))

    ratings = []
    with open('data/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::MovieID::Rating::Timestamp'
                                .split('::'),
                                delimiter='\t')
        for row in reader:
            rating = {
                'fields': {
                    'stars': row['Rating'],
                    'rater': row['UserID'],
                    'movie': row['MovieID'],
                },
                'model': 'ratings.Rating',
            }
            ratings.append(rating)

    with open('ratings/fixtures/ratings.json', 'w') as f:
        f.write(json.dumps(ratings))
