import requests
from credentials import movies_read_access
from flask import request
def get_all_movies(movie_query):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "query": movie_query
    }
    headers = {
        "accept": "application/json",
        "Authorization": F"Bearer {movies_read_access}"
    }
    return requests.get(url, params=params, headers=headers).json()['results']

def get_movie(movie_id):
    url = F"https://api.themoviedb.org/3/movie/{request.args['id']}"
    headers = {
        "accept": "application/json",
        "Authorization": F"Bearer {movies_read_access}"
    }
    return requests.get(url, headers=headers).json()

