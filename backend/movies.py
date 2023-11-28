from pydantic import BaseModel
from typing import Any
from typing import List, Set

class new_movie:
    movie_name: str
    movie_cast: set[str]
    
class Movie(BaseModel):
    id: int
    name: str
    cast: List[str]

class Movies:
#class Movies:

    #_movies: List[ dict[str,List[str]] ]
    
    def __init__(self, movies_file):
        self._movies = []

        count = 0 
        with open(movies_file, encoding="utf-8") as file:
            row_idx = 0
            for line in file:
                if row_idx%3 == 0:
                    movie_name = line.rstrip()
                if row_idx%3 == 1:
                    movie_cast = line.rstrip().split(',')
                if row_idx%3 == 2:
                   
                    self._movies.append(
                        {
                            'id'  : count,
                            'name': movie_name,
                            'cast': movie_cast
                        }
                    )
                    count += 1
                row_idx += 1

if __name__ == "__main__":
    myMovies = Movies('./movies.txt')