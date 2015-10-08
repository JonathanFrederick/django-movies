from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movies/top', views.top_20),
    url(r'^movie/(?P<movie_id>\d+)', views.show_movie, name='movie_detail'),
    url(r'^rater/(?P<rater_id>\d+)', views.show_rater, name='rater_detail')
]
