from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^top-20', views.top_20, name='top_20'),
    url(r'movie/(?P<movie_id>\d+)$', views.movie_detail, name='movie_detail'),
    url(r'rater/(?P<rater_id>\d+)$', views.rater_detail, name='rater_detail')

]
