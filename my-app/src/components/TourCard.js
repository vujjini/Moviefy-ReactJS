import { Paper, Grid, Typography, Box, Rating, createTheme, ThemeProvider } from '@mui/material'
import  AccessTime from '@mui/icons-material/AccessTime'


const theme = createTheme({
    components:{
        MuiTypography: {
            variants :[
                {
                    props:{
                        variant:"body2"
                    },
                    style:{
                        fontSize:11
                    }
                },
                {
                    props:{
                        variant:"body3"
                    },
                    style:{
                        fontSize:9
                    }
                },
            ]
        }
    }
})

const TourCard = ({tour, handleClick}) => {
    const baseURL = "https://image.tmdb.org/t/p/w500/"
    return (
        <Grid item xs={2}>
            <ThemeProvider theme={theme}>
            <Paper elevation={4} square>
            <button onClick={()=>handleClick(tour.title)}>recommend</button>
                {/* <img style={{"width": "100%", "height": "200px", "object-fit":"cover"}} src={tour.poster} alt=''></img> */}
                <img style={{"max-width": "100%", "height": "auto"}} src={`${baseURL}${tour.poster}`} alt=''></img>
                <Box paddingX={1}>
                    <Typography variant="subtitle1" component="h2">
                        {tour.title}
                    </Typography>

                    <Box sx={{
                        display:"flex",
                        alignItems:"center"
                    }}>
                    
                    <AccessTime sx={{ width: 12.5 }}/>
                    </Box>

                    <Box sx={{
                        display:"flex",
                        alignItems:"center"
                    }}
                    marginTop={3}
                    >
                    </Box>   
                </Box>   
            </Paper>
            </ThemeProvider>
        </Grid>
    )
}

export default TourCard