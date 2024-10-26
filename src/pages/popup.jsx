import React, { useState } from 'react'
import './popup.css'

const Popup = () => {
  return (
    <>
      <div className="main-popup">
      <p className="result">Your Result: <span>Cancerous</span></p>
        <div className="boxes">

            <div className = "col gradCol">

            </div>
            <div className = "col gemCol">

            </div>
            <div className = "col resCol">

            </div>
        </div>

      </div>
    </>
  );
}

export default Popup;