from django.contrib import admin
from models import Movie, Rater, Rating
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie', 'title']


class RaterAdmin(admin.ModelAdmin):
    list_display = ['rater']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie, rater, stars']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Rater, RaterAdmin)
admin.site.register(Rating, RatingAdmin)
