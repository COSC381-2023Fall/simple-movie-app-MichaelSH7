from fastapi import FastAPI 
from typing import Union
from movies import Movies
from movies import Movie

moviesApp = FastAPI()

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

#post
#@moviesApp.post("/movies/{movie_id}")
 #   def post_movie(movie_id: int, new_movie: Movie)-> Union[Movie, None]:
