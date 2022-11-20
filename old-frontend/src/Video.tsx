import { Typography } from "@mui/material";
import { Box } from "@mui/system";
import { useEffect } from "react";
import styles from "./Video.module.css"

type VideoProps = {
    video_id: string
}

const Video = ({video_id}: VideoProps) => {

    useEffect(() => {

    }, [video_id])

    return (
        <Box sx={{ padding: "20px 0px"}}>
            <img 
                src={`https://i.ytimg.com/vi/${video_id}/hqdefault.jpg`} 
                alt=""
                className={styles.thumnail}
            />
            <Box sx={{
                display: "flex",
                gap: "14px",
                paddingTop: "16px",
                objectFit: "cover"
            }}>
                <img 
                    src="https://yt3.ggpht.com/r_qpfpVbFmOxx5nG04C3LR06Atd3z3qeN6FwnlKrQZ_8Twpg2Inkxi0QTIHrPFN3RXA2SJci=s68-c-k-c0x00ffffff-no-rj" 
                    alt="" 
                    style={{
                        width: "35px",
                        height: "35px",
                        borderRadius: "100%"
                    }}
                />
                <Box>
                    <Typography sx={{fontWeight: "bold", marginBottom: "7px"}}>
                        Video Title
                    </Typography>
                    <Typography sx={{ color: "#A7A8A8", fontSize: "13px"}}>
                        Channel Name
                    </Typography>
                    <Typography sx={{ color: "#A7A8A8", fontSize: "13px"}}>
                        {`${"7.5k"} views • ${"3 weeks ago"}`}
                    </Typography>
                </Box>
            </Box>
        </Box>
    )
}

export default Video;