import React, { useState, useEffect } from 'react'
import Uploader from '../components/Uploader.jsx';
import { Popup as ReactJSPopup } from 'reactjs-popup'; 
import CustomPopup from './popup.jsx';
import './home.css'

const Home = () => {
  const [buttonPopup, setButtonPopup] = useState(false);
  const [image, setImage] = useState(null)
  const [fileName, setFileName] = useState("No Selected File - ")
  const form = document.getElementById('upload-form');

  const [diagnosis, setDiagnosis] = useState('');
  const [gradcam, setGradcam] = useState('');
  const [gradcamImage, setGradcamImage] = useState('');
  const [explanation, setExplanation] = useState('');
  const [treatment, setTreatment] = useState('');
  const [educationalResources, setEducationalResources] = useState('');
  const [loading, setLoading] = useState(false);
  const [gradcamAnalysis, setGradcamAnalysis] = useState('');

  useEffect(() => {
    console.log('Updated gradcamImage:', gradcamImage);
  }, [gradcamImage]);

  const resetUploader = () => {
    setFileName("No Selected File - ");
    setImage(null);
  };

  return (
    <>
      <h1 className="inter-header title">swida</h1>
      <h2 className="inter-header subtitle">an ai lung cancer assistant</h2>
      <Uploader 
        setButtonPopup={setButtonPopup} 
        setGradcam={setGradcam}
        setDiagnosis={setDiagnosis} 
        setExplanation={setExplanation} 
        setTreatment={setTreatment} 
        resetUploader={resetUploader} 
        setFileName={setFileName} 
        setImage={setImage}
        fileName={fileName}
        image={image}
        form={form}
        gradcamImage={gradcamImage}
        setGradcamImage={setGradcamImage}
        setEducationalResources={setEducationalResources}
        loading={loading}
        setLoading={setLoading}
        setGradcamAnalysis={setGradcamAnalysis}
      />
      <CustomPopup 
        trigger={buttonPopup} 
        setTrigger={setButtonPopup}
        resetUploader={resetUploader}
        form={form}
        diagnosis={diagnosis}
        gradcam={gradcam}
        explanation={explanation}
        treatment={treatment}
        gradcamImage={gradcamImage}
        educationalResources={educationalResources}
        gradcamAnalysis={gradcamAnalysis} />
    </>
  );
}

export default Home;