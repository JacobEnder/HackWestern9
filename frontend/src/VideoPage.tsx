import SkipNextIcon from '@mui/icons-material/SkipNext';
import { Box, Button, Typography } from '@mui/material';
import InfoIcon from '@mui/icons-material/Info';
import { useState, useEffect } from "react";
import { getToxicityFromUrl } from './api';

interface VideoPageProps {
  onSkip: () => void,
  url: string
}

const toxicRating = (score: Number) => {
  if (score > .8) {
    return "Very Toxic";
  } else if (score > 0.5) {
    return "Toxic";
  } else if (score > 0.2) {
    return "Moderately Toxic";
  } else if (score != 0) {
    return "Slightly Toxic";
  } else {
    return "Not Toxic";
  }
};

export default function VideoPage({ onSkip, url }: VideoPageProps) {
  const [score, setScore] = useState(0);
  const [toxicity, setToxicity] = useState(null);

  useEffect(() => {
    getToxicityFromUrl(url)
      .then((data) => {
        setToxicity(data) 
      })
  }, [url])

  return <>
    <Box sx={{}}>
      {toxicity}
      <Box>
        {/* percent and toxicity label */}
        <Typography variant="h1">
          {Math.floor(score / 1) * 100}%
        </Typography>
        <Typography>{toxicRating(score)}</Typography>
      </Box>
      {/* rating/warning */}
      <Box 
        sx={{
          display: "flex",
          gap: "8px",
          padding: "10px 14px",
          borderRadius: "12px",
          alignItems: "center",
          margin: "10px 0px",
          backgroundColor: "#272727"
        }}
      >
        <InfoIcon />
        <Typography sx={{}}>
          {"This video is rated "}
          <span style={{fontWeight: "500"}}>{toxicRating(score)}</span>.<br/>
            {score != 0 && "Consider watching another video."}
        </Typography>
      </Box>
      <Button variant="contained" endIcon={<SkipNextIcon />} onClick={onSkip}>
        Skip Toxicity
      </Button>
    </Box>
  </>
}