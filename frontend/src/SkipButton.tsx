import SkipNextIcon from '@mui/icons-material/SkipNext';
import { Button } from '@mui/material';

export default function SkipButton() {
  return <>
    <Button variant="contained" endIcon={<SkipNextIcon />}>
      Skip Toxicity
    </Button>
  </>
}