from flask import Flask, jsonify, request
from storage import all_movies,liked_movies,not_liked_movies,not_watched_movies
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-movie")

def get_movie():
    movie_data = {
        "title": all_movies[0][19],
        "poster_link": all_movies[0][27],
        "release_date": all_movies[0][13],
        "duration": all_movies[0][15],
        "rating": all_movies[0][20],
        "overview": all_movies[0][9]
    }
    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route("/liked-movies", methods = ["POST"])

def liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201


@app.route("/not_liked-movies", methods = ["POST"])

def not_liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201


@app.route("/not_watched-movies", methods = ["POST"])

def not_watched_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_watched_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run()
