# import csv
# import json
#
#
# def load_movies():
#     movies = []
#     with open('data/movies.dat', encoding='windows-1252') as f:
#         reader = csv.DictReader([line.replace('::', '\t') for line in f],
#                                 fieldnames=['movie_id', 'title', 'genres'],
#                                 delimiter='\t')
#         for line in reader:
#             movie = {
#                 'fields': {
#                     'title': line['title']
#                 },
#                 'model': 'ratingsdb.Movie',
#                 'pk': int(line['movie_id'])
#             }
#             movies.append(movie)
#
#     with open('fixtures/movies.json', 'w') as f:
#         f.write(json.dumps(movies))
#
#
# def load_raters():
#     from faker import Faker
#     import random
#
#     # from django.contrib.auth.models import User
#
#     fake = Faker()
#     raters = []
#     with open('data/users.dat') as f:
#         reader = csv.DictReader([line.replace('::', '\t') for line in f],
#                                 fieldnames=['UserID', 'Gender', 'Age',
#                                             'Occupation', 'Zip-code'],
#                                 delimiter='\t')
#         for line in reader:
#             # User.objects.create_user(username=fake.username() +
#             #                          str(random.randint(10, 99)),
#             #                          email=fake.email(),
#             #                          password='password',
#             #                          pk=line['UserID'])
#             rater = {
#                 'fields': {
#                     'gender': line['Gender'],
#                     'age': line['Age'],
#                     'occupation': line['Occupation'],
#                     'zipcode': line['Zip-code']
#
#                 },
#                 'model': 'ratingsdb.Rater',
#                 'pk': line['UserID']
#             }
#             raters.append(rater)
#
#     with open('fixtures/raters.json', 'w') as f:
#         f.write(json.dumps(raters))
#
# load_movies()
# load_raters()
