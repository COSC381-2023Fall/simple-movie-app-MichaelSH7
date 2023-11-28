class Movies:
    def __init__(self, movies_file):
        self._movies = []

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
                            'name': movie_name,
                            'cast': movie_cast
                        }
                    )
                    movie_name = None
                    movie_cast = None
                row_idx += 1

        if movie_name and movie_cast:
            # Add the last movie to the list
            self._movies.append(
                {
                    'name': movie_name,
                    'cast': movie_cast
                }
            )
            
    def search_movies_by_name(self, keyword):
        matched_movies = []
        for movies in self._movies:
            if keyword.lower() in movies['name'].lower():
                matched_movies.append(movies['name'])

        if matched_movies:
            for movie_name in matched_movies:
                print(movie_name)
        else:
            print("No matching movies found.")

    def list_all_movies(self) :
        for movies in self._movies:
            print(movies['name'])


    def search_movies_by_cast(self, keyword):
        matched_movies = []

        for movies in self._movies:
            matched_cast = []
            for actor in movies['cast']:
                if keyword.lower() in actor.lower():
                    matched_cast.append(actor)
            if matched_cast:
                matched_movies.append({
                    'name': movies['name'],
                    'cast': matched_cast
                })

        if matched_movies:
            for movies in matched_movies:
                print(movies['name'])
                print(movies['cast'])
        else:
            print("\nNo movies matched the search keyword")
            

if __name__ == "__main__":
    movies = Movies('./movies.txt')
