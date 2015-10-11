from django.test import TestCase
from .models import *

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
        Movie.objects.create(title='TEST', pk=1)
        self.assertEquals(Movie.objects.get(pk=1).title, 'TEST')
        self.assertEquals(Movie.objects.get(title='TEST').pk, 1)
        self.assertNotEquals(Movie.objects.get(title='TEST').pk, 2)

    # def test_rating_creation(self):
    #     test_rat = Rating.objects.create(stars=5, movie=43, rater=210, pk=1)
    #     self.assertEquals(Rating.objects.get(pk=1).stars, 5)
    #     self.assertEquals(Rating.objects.get(pk=1).movie, 43)
    #     self.assertEquals(Rating.objects.get(pk=1).rater, 210)
    #     self.assertEquals(Rating.objects.get(movie=43).pk, 1)
    #     self.assertNotEquals(Rating.objects.get(movie=43).pk, 2)

    def test_rater_creation(self):
        test_user = User.objects.create_user(pk=1,
                                             username='tester',
                                             email='test@gmail.com',
                                             password='password')
        Rater.objects.create(pk=1, gender='M', zipcode='55555',
                             occupation=6, age=35, user=test_user)
        self.assertEqual(Rater.objects.get(pk=1).gender, 'M')
        self.assertEqual(Rater.objects.get(pk=1).zipcode, '55555')
        self.assertEqual(Rater.objects.get(pk=1).occupation, 6)
        self.assertEqual(Rater.objects.get(pk=1).age, 35)
        self.assertGreater(User.objects.count(), 0)
