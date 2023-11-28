from fastapi import FastAPI 
from typing import Union
from movies import Movies

moviesApp = FastAPI()

movies = Movies('./movies.txt')

@moviesApp.get("/movies/{movie_id}")
def Finding_Movie_id(movie_id: str):
    if 0 <= int(movie_id) < len(movies._movies):
        return movies._movies[int(movie_id)]
    else:
        return None