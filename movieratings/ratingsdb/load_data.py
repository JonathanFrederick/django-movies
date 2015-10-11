def load_movies():
    with open('data/movies.dat', encoding='windows-1252') as f:
        movies = [line.replace('::', '\t') for line in f]
        print(movies)

load_movies()
