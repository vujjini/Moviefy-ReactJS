import logo from './logo.svg';
import './App.css';
import Home from './pages/home'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Navbar from './components/Appbar'
import Form from './pages/form';

function App() {
  return (
    // 
    <div>
      <BrowserRouter>
      <Navbar/>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route path="/option1" element={<Form/>}></Route>
        </Routes>
      </BrowserRouter>

    </div>
  )
};

export default App;