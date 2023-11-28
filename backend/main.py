from fastapi import FastAPI 
from typing import Union
from movies import Movies
from movies import Movie

moviesApp = FastAPI()

movies = Movies('./movies.txt') 

@moviesApp.get("/movies/{movie_id}")
def Finding_Movie_id(movie_id: int) -> Union[Movie, None]:
    for i in range(0,len(movies._movies),1):
        if (movies._movies[i]['id']==movie_id):
            return movies._movies[i]
# update?

@moviesApp.put("/movies/{movie_id}")
def add_movie(movie_id: int, new_movie: Movie)-> Union[Movie, None]:
    for i in range (0, len(movies._movies),1):
        if(movies._movies[i]['id']==movie_id):
            movies._movies [i]['name'] = new_movie.name
            movies._movies [i]['cast'] = new_movie.cast
            return {
                "id": new_movie.id,
                    "name": new_movie.name,
                    "cast": new_movie.cast
            }
