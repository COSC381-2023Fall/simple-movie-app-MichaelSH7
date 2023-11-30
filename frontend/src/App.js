
import './App.css';
import { useEffect, useState } from 'react';
import LocalMoivesIcon from '@mui/icons-material/LocalMovies';
import {TextField, List, ListItem, ListItemIcon, ListItemText} from '@mui/material';


function App() {
  
  const [movieId, setMovieId]=useState("16") 
  const [movie, setMovie] = useState(null)

  useEffect(() => {
    if(movieId==""){
      setMovie(null);
    } else {
      fetch (`http://localhost:8000/movies/${movieId}`)
      .then ( result => result.json() )
      .then ( result => {
        console.log (`http://localhost:8000/movies/${movieId}`)
        setMovie(result);
      });
    }
    console.log(movieId);
  }, [movieId]);

  useEffect(() => {
    console.log(movie);
  }, [movie]);
 



  return (
    <div className="App">
      <header className="App-header">
        <TextField  id="outlined-basic" label ="MovieId" 
          variant ="outlined" color ="warning" focuse value={movieId}
          onChange={e=> setMovieId(e.target.value)}
          /> 
          <List>
            { movie &&
            <ListItem>
                <ListItemIcon> 
                  <LocalMoivesIcon />
                </ListItemIcon>
                <ListItemText primary = {movie['name']}/>
              </ListItem>}
          </List>
      </header>
    </div>
  );
}

export default App;
