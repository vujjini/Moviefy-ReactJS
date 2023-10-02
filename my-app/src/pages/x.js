import React from "react";
import '../index.css'
import TourCard from "./Components/TourCard";
import { Container, Typography, Grid } from '@mui/material'
import cities from '../data.json'

const Home = () => {
    
    return (
        <>
            <Container sx={{
                marginY:5
            }}>
            {cities.map((city) => (
                <>
                <Typography
                    variant="h5"
                    component="h2"
                    marginTop={5}
                    marginBottom={4} 
                >
                    Top spots in {city.name}
                </Typography>
                <Grid container spacing={2}>
                    {city.tours.map((tour, index) => (
                        <TourCard tour={tour} key={index}/>
                    ))}
                </Grid>
                </>
            ))}
            </Container>
        </>
    )
    
}

export default Home