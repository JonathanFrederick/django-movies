from django.test import TestCase
from .models import *

# Create your tests here.


class MovieTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(pk=1,
                                             username='tester',
                                             email='test@gmail.com',
                                             password='password')
        Rating.objects.create(stars=5,
                              movie=Movie.objects.create(title='TEST', pk=1),
                              rater=Rater.objects.create(pk=1, gender='M',
                                                         zipcode='55555',
                                                         occupation=6, age=35,
                                                         user=test_user),
                              pk=1)

    def test_movie_creation(self):
        self.assertEquals(Movie.objects.get(pk=1).title, 'TEST')
        self.assertEquals(Movie.objects.get(title='TEST').pk, 1)
        self.assertNotEquals(Movie.objects.get(title='TEST').pk, 2)

    def test_rating_creation(self):
        self.assertEquals(Rating.objects.get(pk=1).stars, 5)
        self.assertEquals(Rating.objects.get(pk=1).movie.pk, 1)
        self.assertEquals(Rating.objects.get(pk=1).rater.pk, 1)

    def test_rater_creation(self):
        self.assertEqual(Rater.objects.get(pk=1).gender, 'M')
        self.assertEqual(Rater.objects.get(pk=1).zipcode, '55555')
        self.assertEqual(Rater.objects.get(pk=1).occupation, 6)
        self.assertEqual(Rater.objects.get(pk=1).age, 35)
        self.assertGreater(User.objects.count(), 0)
