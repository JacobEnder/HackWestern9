import { Box, Chip, Typography } from "@mui/material";
import DangerousIcon from '@mui/icons-material/Dangerous';

type ScoresProps = {
    video_id: string
}

const Scores = ({video_id}: ScoresProps) => {
    
    return (
        <Box
            sx={{
                padding: "0px 25px",
                width: "270px"
            }}
        >
            <Typography 
                sx={{
                    fontSize: "18px",
                    fontWeight: "700"
                }}
            >
                Scores
            </Typography>
            <Typography sx={{color: "#A7A8A8", fontSize: "15px"}}>
                Our percentage rating for this video's content
            </Typography>
            <Box sx={{paddingTop: "15px"}}>
                <Box>
                    <Typography
                        sx={{
                            padding: "5px"
                        }}
                    >
                        Toxicity
                    </Typography>
                    <Chip label={"75%"} icon={<DangerousIcon/>}
                        sx={{
                            backgroundColor: "#434343",
                            color: "white"
                        }}
                    />
                </Box>
            </Box>
        </Box>
    )
}

export default Scores;