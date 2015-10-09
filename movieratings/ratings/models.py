from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Rater(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    NOT_GIVEN = 'X'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NOT_GIVEN, 'X'),)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              default=NOT_GIVEN)
    zipcode = models.CharField(max_length=5, default='00000')
    age = models.PositiveIntegerField(default='0')
    occupation = models.CharField(max_length=40, default='00')
    # profile = models.OneToOneField(User, null=True, primary_key=True)

    def __str__(self):
        return str(self.id)


class Movie(models.Model):
    title = models.CharField(max_length=215)

    def average_rating(self):
        # give key because aggregate returns as database entry
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']

    def __str__(self):
        return str(self.id) + ' - ' + str(self.title)


class Rating(models.Model):
    stars = models.SmallIntegerField()  # change to PositiveSmallIntegerField
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return '{}: {} ({})'.format(str(self.movie),
                                    str(self.stars),
                                    str(self.rater))


def create_fake_user(user_id, fake):
    return {'fields': {'username': fake.user_name(),
                       'email': fake.email(),
                       'password':'password'},
            'model': 'users.Profile',
            'pk': user_id
            }
def load_initial_data():
    import csv
    import json
    from faker import Faker
    from users.models import Profile
    # from django.contrib.auth.models import User

    fake = Faker()
    raters = []
    profiles = []
    # list({User.objects
    #                  .create_user(username=fake.user_name(),
    #                               email=fake.email(),
    #                               password='password') for _ in range(9001)})
    with open('data/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='\t')
        for row in reader:
            rater = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                    # 'profile': profiles.pop(0)
                    # User.objects
                    #                .create_user(username=fake.user_name(),
                    #                             email=fake.email(),
                    #                             password='password')
                },
                'model': 'ratings.Rater',
                'pk': int(row['UserID']),
            }
            raters.append(rater)
            try:
                new_profile = create_fake_user(int(row['UserID']), fake)
            except:
                print("HI", end=' ')
                fake = Faker()
                new_profile = create_fake_user(int(row['UserID']), fake)
            # new_profile.save()
            profiles.append(new_profile)
    with open('ratings/fixtures/raters.json', 'w') as f:
        f.write(json.dumps(raters))
    with open('ratings/fixtures/profiles.json', 'w') as f:
        f.write(json.dumps(profiles))

    movies = []
    with open('data/movies.dat', encoding='windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genres'
                                .split('::'),
                                delimiter='\t')
        for row in reader:
            movie = {
                'fields': {
                    'title': row['Title'],
                },
                'model': 'ratings.Movie',
                'pk': int(row['MovieID'])
            }
            movies.append(movie)

    with open('ratings/fixtures/movies.json', 'w') as f:
        f.write(json.dumps(movies))

    ratings = []
    with open('data/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::MovieID::Rating::Timestamp'
                                .split('::'),
                                delimiter='\t')
        for row in reader:
            rating = {
                'fields': {
                    'stars': row['Rating'],
                    'rater': row['UserID'],
                    'movie': row['MovieID'],
                },
                'model': 'ratings.Rating',
            }
            ratings.append(rating)

    with open('ratings/fixtures/ratings.json', 'w') as f:
        f.write(json.dumps(ratings))
