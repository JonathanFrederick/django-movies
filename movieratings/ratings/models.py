from django.db import models


# Create your models here.
class Rater(models.Model):
    rater = models.IntegerField()

    def __str__(self):
        return str(self.rater)


class Movie(models.Model):
    title = models.CharField(max_length=215)
    movie = models.IntegerField()

    def __str__(self):
        return str(self.movie) + ' - ' + self.title


class Rating(models.Model):
    stars = models.SmallIntegerField()
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return self.movie + ': ' + str(self.stars) + '(' + self.rater + ')'
