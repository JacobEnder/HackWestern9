import { useState, useEffect } from "react";

const serverUrl = "http://localhost:5000/s";

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

interface VideoInfoProps {
  vid: string
};
export default function VideoInfo({ vid } : VideoInfoProps) {
    const [score, setScore] = useState(0);

    useEffect(() => {
        const urlParams = new URLSearchParams({
            yt_code: vid,
          });
        fetch(`${serverUrl}?${urlParams.toString()}`)
          .then((response) => response.json())
          .then((data) => console.log(data))
    }, [])
    return (
        <>
            henlo
        </>
    )
}