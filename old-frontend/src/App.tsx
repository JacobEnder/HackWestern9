import { useState } from 'react'
import './App.css'
import NoVideoPage from './NoVideoPage';
import VideoPage from "./VideoPage";

function App() {

  const [vid, setvid] = useState("video");
  console.log(document.getElementById("content"));

  return (
    <div className="App">
      <header className="App-header">
        {vid ? (
          <VideoPage onSkip={() => alert("skipping!")}/>
        ) : (
          <NoVideoPage />
        )}
      </header>
    </div>
  )
}

export default App
