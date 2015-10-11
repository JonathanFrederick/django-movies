from django.test import TestCase
from .models import Movie
# Create your tests here.


class MovieTestCase(TestCase):
    # def set_up(self):
    # test_mov = Movie.objects.create(title='TEST', pk=1)
    # test_mov.save()
    # print('HIHIHIHIHIHIHIHIH')


        # test_mov = Movie()
        # test_mov.title = 'TEST'
        # test_mov.pk = 1
    def test_movie_creation(self):
        test_mov = Movie.objects.create(title='TEST', pk=1)
        self.assertEquals(Movie.objects.get(pk=1).title, 'TEST')
        self.assertEquals(Movie.objects.get(title='TEST').pk, 1)
