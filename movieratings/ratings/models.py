from django.db import models


# Create your models here.
class Rater(models.Model):
    rater = models.IntegerField()





class Movie(models.Model): # 215
    title = models.CharField(max_length=215)
    movie = models.IntegerField()




# class Rating()
