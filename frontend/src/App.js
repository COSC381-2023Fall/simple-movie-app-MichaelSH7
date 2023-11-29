import logo from './logo.svg';
import {TextField} from '@mui/material'
import './App.css';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <TextField  id="outlined-basic" label ="MovieId" 
          variant ="outlined"/>  
      </header>
    </div>
  );
}

export default App;
