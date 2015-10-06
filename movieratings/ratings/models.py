from django.db import models


# Create your models here.
class Rater(models.Model):
    rater = models.IntegerField()





class Movie(models.Model):
    title = models.CharField(max_length=215)
    movie = models.IntegerField()




class Rating(models.Model):
    stars = models.SmallIntegerField()
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
