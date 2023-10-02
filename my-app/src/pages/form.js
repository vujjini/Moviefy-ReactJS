import React, { useState } from 'react';
import {Grid} from '@mui/material'
import { Container } from '@mui/material';
import TourCard from '../components/TourCard';

function Form() {
  const [movie_list, setMovie_list] = useState([])
  const [input, setInput] = useState({});
  const [title, setTitle] = useState("");
  const [poster, setPoster] = useState("");

  const handleChange = event => {
    setInput({
      ...input,
      [event.target.name]: event.target.value
    });
  };

  const handleSubmit = event => {
    event.preventDefault();
    fetch('http://127.0.0.1:5000/moviename', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(input)
    })
      .then(res => res.json())
      .then(data => {
        setMovie_list(data)
        console.log(data)      
    })
      .catch(error => console.error(error));
  };
  const getMovies = async (input) => {

    const res = await fetch('http://127.0.0.1:5000/moviename', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(input)
    })
    .then(res => res.json())
      .then(data => {
        setMovie_list(data)
        console.log(data)      
    })
    
  }
  const handleClick = item => {
      console.log(item)
      getMovies({ 'title1': item })
      
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="text" name="title1" onChange={handleChange} />
        <input type="text" name="title2" onChange={handleChange} />
        <button type="submit">Submit</button>
      </form>
      {movie_list ? (
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
    </>
      ) : null}
    </div>
  );
}

function Child(props) {
  const baseURL = "https://image.tmdb.org/t/p/w500/"
  const picture = props.pic
  const finalURL = `${baseURL}${picture}`;
  return (
    <div>
      <p>Output data: {props.output}</p>
      <img src={finalURL} alt="" />
    </div>
  );
}


export default Form;

// export default function Form(props) {
//     const [title, setTitle] = useState('')
//     // const [body, setBody] = useState('')

//     const insertArticle = () =>{
//       APIService.InsertArticle({title})
//       .then((response) => props.insertedArticle(response))
//       .catch(error => console.log('error',error))
//     }

//     const handleSubmit=(event)=>{ 
//       event.preventDefault()
//       insertArticle()
//       setTitle('')
//     }

//   return (
//     <div className="shadow p-4">

//         <form onSubmit = {handleSubmit} >

//           <label htmlFor="title" className="form-label">Title</label>
//           <input 
//           type="text"
//           placeholder ="Enter title"
//           value={title}
//           onChange={(e)=>setTitle(e.target.value)}
//           required
//           />

//           <button 
//           className="btn btn-primary mt-2"
//           >
//           BRUH</button>
          
//         </form>
              

//     </div>
//   )}