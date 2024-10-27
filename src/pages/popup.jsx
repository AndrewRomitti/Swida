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
  const diagnosisColor = props.diagnosis === 'Normal' ? 'green' : 'red';
  console.log("Gradcam Url:",props.gradcamImage);

  return props.trigger ? (
    <>
    <div className="popup">
      <div className="main-popup">
        <div className="title">
          <h1 className="inter-header">Your Result: <br/><span style={{ color: diagnosisColor }}>{diagnosisLabel}</span></h1>
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
              <div className="gradcam">
              <h2 className="inter-subheader">Grad-CAM Visualization</h2>
              {props.gradcamImage ? (
                <div>
                  <img src={props.gradcamImage} alt="Grad-CAM" style={{ maxWidth: '100%', marginTop: '20px' }} />
                  <ReactMarkdown>{ props.gradcamAnalysis || "No analysis available."}</ReactMarkdown>
                </div>
                ) : (
                  <p>No Grad-CAM image available.</p>
                )}
              </div>
            </div>
            )}
          <div className="treatment">
            <h2 className="inter-subheader">{props.diagnosis === 'Normal' ? 'Prevention' : 'Treatment'}</h2>
            <ReactMarkdown>{ props.treatment }</ReactMarkdown>
          </div>
          <div className="educational-resources">
            <h2 className="inter-subheader">Educational Resources</h2>
            <ReactMarkdown>{ props.educationalResources[0] }</ReactMarkdown>
            <ReactMarkdown>{ props.educationalResources[1] }</ReactMarkdown>
            <ReactMarkdown>{ props.educationalResources[2] }</ReactMarkdown>
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