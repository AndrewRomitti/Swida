import React, { useState } from 'react'
import ReactMarkdown from 'react-markdown';
import './popup.css'

const CustomPopup = (props) => {
  const closePopup = () => {
    props.setTrigger(false); 
    props.resetUploader();
    props.form.reset();
  };

  const diagnosisLabel = props.diagnosis === 'Normal' ? 'Healthy' : 'Cancer Detected';

  return props.trigger ? (
    <>
    <div className="popup">
      <div className="main-popup">
        <div className="title">
          <h1 className="inter-header">Your Result: <br/>{diagnosisLabel}</h1>
        </div>
        <div className="result-container">
          {props.diagnosis === 'Normal' ? (
            <h1 className="inter-header">Healthy Lungs.</h1>
            ) : (
            <div>
              <h1 className="inter-header" id="diagnosis-header">Diagnosis: {props.diagnosis}</h1>
              <div className="explanation">
              <h2 className="inter-subheader">Explanation</h2>
              <ReactMarkdown>{ props.explanation }</ReactMarkdown>
              </div>
            </div>
            )}
          <div className="treatment">
            <h2 className="inter-subheader">{props.diagnosis === 'Normal' ? 'Prevention' : 'Treatment'}</h2>
            <ReactMarkdown>{ props.treatment }</ReactMarkdown>
          </div>
          <div className="educational-resources">
            <h2 className="inter-subheader">Educational Resources</h2>
          </div>
        </div>
        <button className="close-popup" onClick={closePopup}>close</button>
        { props.children }
      </div>
    </div>
    </> 
    ) : null;
}

export default CustomPopup;