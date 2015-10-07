from django.db import models


# Create your models here.
class Rater(models.Model):
    def __str__(self):
        return str(self.id)


class Movie(models.Model):
    title = models.CharField(max_length=215)

    def average_rating(self):
        # give key because aggregate returns as database entry
        self.rating_set.aggregate(models.Avg('stars'))['stars_avg']

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

    movies = []
    raters = []

    with open('data/movies.csv') as f:
        reader = csv.DictReader(f, fieldnames=['movieId', 'title', 'genres'])
        for row in reader:
            movie = {
                'fields': {
                    'title': row['title']
                },
                'model': 'ratings.Movie',
                'pk': row['movieId']
            }
            movies.append(movie)

    with open('movies.json', 'w') as f:
        f.write(json.dumps(movies))

    print(json.dumps(movies, sort_keys=True, indent=4, separators=(',', ': ')))
