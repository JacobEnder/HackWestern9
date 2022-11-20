import React, { useState, useEffect } from 'react';
import { TextField, Box } from '@mui/material';
import Youtube from 'react-youtube';
import VideoInfo from './VideoInfo';
import './App.css';

function getIdFromUrl(url: string) {
  const regExp =
    /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
  const match = url.match(regExp);
  return match && match[7].length == 11 ? match[7] : "";
}

function App() {
  
  const [videoUrl, setVideoUrl] = useState<string>("https://www.youtube.com/watch?v=5wyVqC0Fb_w");

  const onTextFieldChange = (event: React.ChangeEvent<HTMLInputElement>) => {
      setVideoUrl(event.target.value);
  }

  return (
    <div className="App">
      <header className="App-header"></header>

        <TextField
          id="address"
          label="Entry Address"
          onChange={onTextFieldChange}
        />


        {videoUrl && (
          <Box>
            <Youtube
              videoId={getIdFromUrl(videoUrl)}
            />
            <VideoInfo vid={getIdFromUrl(videoUrl)} />
          </Box>
        )}

      <header className="App-header"></header>
    </div>
  );
}

export default App;
