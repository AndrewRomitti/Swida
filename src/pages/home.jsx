import React, { useState } from 'react'
import Uploader from '../components/Uploader.jsx';
import './home.css'

const Home = () => {
  return (
    <>
      <h1 className="inter-header">swida</h1>
      <h2 className="inter-header">an ai lung cancer assistant</h2>
      <Uploader />
    </>
  );
}

export default Home;