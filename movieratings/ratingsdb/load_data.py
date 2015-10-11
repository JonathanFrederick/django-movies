import csv, json


def load_movies():
    movies = []
    with open('data/movies.dat', encoding='windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames=['movie_id', 'title', 'genres'],
                                delimiter='\t')
        for line in reader:
            movie = {
                'fields': {
                    'title': line['title']
                },
                'model': 'ratingsdb.Movie',
                'pk': int(line['movie_id'])
            }
            movies.append(movie)

    with open('fixtures/movies.json', 'w') as f:
        f.write(json.dumps(movies))


load_movies()
