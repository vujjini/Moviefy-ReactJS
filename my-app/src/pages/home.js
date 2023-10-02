// import React, { useState, useEffect } from 'react';
// import Card from '@mui/material/Card';
// import CardActions from '@mui/material/CardActions';
// import CardContent from '@mui/material/CardContent';
// import CardMedia from '@mui/material/CardMedia';
// import Button from '@mui/material/Button';
// import Typography from '@mui/material/Typography';
// import { Link } from 'react-router-dom';

// export default function Home() {
//   const [data, setData] = useState([]);
//   const [input, setInput] = useState({});
//   useEffect(() => {
//     async function fetchData() {
//       const response = await fetch('http://127.0.0.1:5000/home');
//       const result = await response.json();
//       setData(result);
//     }
//     fetchData();
//   }, []);
//   console.log(data)
//   const handleClick = event => {
//     event.preventDefault();
//     fetch('http://127.0.0.1:5000/moviename', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify(input)
//     })
//       .then(res => res.json())
//   };
//   const baseURL = "https://image.tmdb.org/t/p/w500/"
//   return (
//     <div>
//       {data.map(item => (
//         <Card sx={{ maxWidth: 345 }} key={item.id}>
//         <CardMedia
//           sx={{ height: 140 }}
//           image={item.poster}
//           title={item.name}
//         />
//         <CardContent>
//           <Typography gutterBottom variant="h5" component="div">
//           {item.name}
//           </Typography>
//         </CardContent>
//         <CardActions>
//         <Button size="small" onClick={() => handleClick(item.name)}>
//               Recommendations
//           </Button>
//       </CardActions>
//       </Card>
      
//     ))}
//     </div>
    
//   );
// }
import React, { useState, useEffect } from 'react';
import Card from '@mui/material/Card';
import {Grid} from '@mui/material'
import { Container } from '@mui/material';
import TourCard from '../components/TourCard';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Link } from 'react-router-dom';


const Loading = () => {
  return (
    <div className="loading-overlay">
      <div className="loading-spinner"></div>
      <p>Loading...</p>
    </div>
  );
};


export default function Home() {
  const [isLoading, setIsLoading] = useState(false);

  const [data, setData] = useState([]);
  const [input, setInput] = useState({});
  // const [title, setTitle] = useState("");
  // const [poster, setPoster] = useState("");
  const [movie_list, setMovie_list] = useState([])
  useEffect(() => {
    setIsLoading(true);
    
    async function fetchData() {
      const response = await fetch('http://127.0.0.1:5000/home');
      const result = await response.json();
      setMovie_list(result);
      setIsLoading(false);
    }
    fetchData();
  }, []);

  const getMovies = async (input) => {
    setIsLoading(true); // Set loading state to true before sending the request
  
    try {
      const res = await fetch('http://127.0.0.1:5000/moviename', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(input)
      });
  
      if (res.ok) {
        const data = await res.json();
        setMovie_list(data);
        console.log(data);
      } else {
        // Handle the error here
        console.error('Error fetching data');
      }
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setIsLoading(false); // Set loading state to false after the request is completedd
    }
  };
  
  const handleClick = item => {
      console.log(item)
      getMovies({ 'title1': item })
      
  };
  
 


  

  return (
    <>
    <Container sx={{
        marginY:5
    }}>
    <Grid container spacing={2}>
      
      {movie_list.map(movie =>  (
        <TourCard tour={movie} handleClick={handleClick}/>
      ))}
    </Grid>
    </Container>
    {isLoading && <Loading />}
</>
  )
  // return (
  //   <div>
  //     {data.map(item => (
  //       <Card sx={{ maxWidth: 345 }} key={item.id}>
  //       <CardMedia
  //         sx={{ height: 140 }}
  //         image={item.poster}
  //         title={item.name}
  //       />
  //       <CardContent>
  //         <Typography gutterBottom variant="h5" component="div">
  //         {item.name}
  //         </Typography>
  //       </CardContent>
  //       <CardActions>
  //       <Button size="small" onClick={() => handleClick(item.name)}>
  //             Recommendations
  //         </Button>
  //     </CardActions>
  //     </Card>
      
  //   ))}
  //   </div>
    
  // );
}






