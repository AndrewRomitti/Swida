import React, { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/home.jsx';
import Popup from './pages/popup.jsx';
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/popup" element={<Popup />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
