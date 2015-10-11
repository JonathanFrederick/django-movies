import csv

def load_movies():
    with open('data/movies.dat', encoding='windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames=['movie_id', 'title', 'genres'],
                                delimiter='\t')
        for line in reader:
            print(line)

load_movies()
