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
