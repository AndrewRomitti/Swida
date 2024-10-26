import React, { useState } from 'react'
import './popup.css'

const Popup = () => {
  return (
    <>
      <div className="main-popup">
      <p className="result">Your Result: <span className="binaryR">Cancerous</span></p>
        <div className="boxes">

            <div className = "col gradCol">
                <p className="colHead">Explanation</p>
                <div className="colBody">
                    <p>Your result returned <strong>large cell carcinoma</strong>, this is a cancer that is diagnosed to 42.6% of patients. Below is a heatmap that explains where the AI thinks is most important to examine</p>
                </div>
                <div className="colImg">
                    <div className="plcImg">
                        
                    </div>
                </div>
            </div>
            <div className = "col gemCol">
                <p className="colHead">Treatment</p>
            </div>
            <div className = "col resCol">
                <p className="colHead">Educational Resources</p>
            </div>
        </div>

      </div>
    </>
  );
}

export default Popup;