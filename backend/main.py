from fastapi import FastAPI 
from typing import Union
from movies import Movies
from movies import Movie
from movies import new_movie

moviesApp = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost:3000",
]
moviesApp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
movies = Movies('./movies.txt') 
# get
@moviesApp.get("/movies/{movie_id}")
def Finding_Movie_id(movie_id: int) -> Union[Movie, None]:
    for i in range(0,len(movies._movies),1):
        if (movies._movies[i]['id']==movie_id):
            return movies._movies[i]

# update
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

#delete
@moviesApp.delete("/movies/{movie_id}")
def delete_movie(movie_id: int) -> Union[Movie, None]:
    
    for i in range(0, len(movies._movies),1):
      
        if (movies._movies[i]['id'] == movie_id):
      
          id = movies._movies[i]['id']
          name = str(movies._movies[i]['name'])
          
          cast=movies._movies[i]['cast']
    
          movies._movies.remove(movies._movies[i])
          
          return {
                "id": id,
                    "name": name,
                    "cast": cast
            }
    else:
        return None

# post
@moviesApp.post("/movies")
def post_movie(added_movie: new_movie) -> Union[Movie, None]:
    newid = len(movies._movies) + 1
    the_new_movie = Movie(
        id=newid,
        name=added_movie.movie_name,
        cast=added_movie.movie_cast
    )
    movies._movies.append({
        'id': the_new_movie.id,
        'name': the_new_movie.name,
        'cast': the_new_movie.cast
    })
    return {
        'id': the_new_movie.id,
        'name': the_new_movie.name,
        'cast': the_new_movie.cast
    }
