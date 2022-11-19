import { useState } from 'react'
import './App.css'
import Filters from './Filters';
import Scores from './Scores';
import Video from './Video'

function App() {

  const [vid, setvid] = useState("wchvfDOuC0c");

  return (
    <div className="App">
      <header className="App-header">
		    <Video video_id={vid}/>
        <Scores video_id={vid}/>
        <Filters />
      </header>
    </div>
  )
}

export default App
