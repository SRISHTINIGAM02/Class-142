import csv

all_movies = []

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
not_watched_movies = []
