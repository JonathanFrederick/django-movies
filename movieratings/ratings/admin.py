from django.contrib import admin
from .models import Movie, Rater, Rating
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie', 'title']


class RaterAdmin(admin.ModelAdmin):
    list_display = ['rater']  # just 'id'


class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'rater', 'stars']


admin.site.register(Movie, MovieAdmin)  # don't need Admin here
admin.site.register(Rater, RaterAdmin)  # don't need Admin here
admin.site.register(Rating, RatingAdmin)
