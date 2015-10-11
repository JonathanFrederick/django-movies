def load_movies():
    with open('data/movies.dat', encoding='windows-1252') as f:
        for line in f:
            print(line)
            
load_movies()
