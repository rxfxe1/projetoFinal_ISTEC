import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Menu from './components/Menu';
import Orders from './components/Orders';
import ReservationPage from './components/ReservationPage';

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" exact element={<Home />} />
        <Route path="/menu" exact element={<Menu />} />
        <Route path="/orders" exact element={<Orders />} />
        <Route path="/reserve" element={<ReservationPage />} />
      </Routes>
    </Router>
  );
};

export default App;
