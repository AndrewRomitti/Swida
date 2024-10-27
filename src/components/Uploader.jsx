import React, { useState} from 'react'
import './Uploader.css'
import { MdCloudUpload, MdDelete} from 'react-icons/md'
import { AiFillFileImage } from 'react-icons/ai'

function Uploader({ setButtonPopup, setFileName, setImage, fileName, form, setDiagnosis, setGradcam, setExplanation, setTreatment, setGradcamImage, setEducationalResources}) {
    const [errorMessage, setErrorMessage] = useState('')

    const handleUploadImage = (ev) => {
        ev.preventDefault();

        const fileInput = document.getElementById('input-file');
        const data = new FormData();
        data.append('file', fileInput.files[0]);

        fetch('http://127.0.0.1:5001/upload', {
            method: 'POST',
            body: data,
        })
        .then((response) => response.json())
        .then((body) => {
            console.log('Upload successful:', body);
            setDiagnosis(body.diagnosis); 
            setGradcam(body.gradcam);
            setExplanation(body.explanation);
            setTreatment(body.treatment);
            setButtonPopup(true);
            setErrorMessage('');
            setEducationalResources(body.resources);

            if (body.gradcam) {
                const image = `data:image/jpeg;base64,${body.gradcam.trim()}`;;
                setGradcamImage(image);
                console.log("Gradcam Image:",image)
            }
        })
        .catch((error) => {
            console.error('Upload failed:', error);
            setErrorMessage('Upload failed. Please try again.');
        });
    };


    return (
        <>
        <form id="upload-form" onSubmit={handleUploadImage}>
            <label htmlFor="input-file" id="drop-area">
            <input type="file" accept="image/jpeg, image/png, image/jpg" id="input-file" onClick = { (event) => { event.target.value = null; }}  
            hidden onChange={({ target: {files}}) => {
                files[0] && setFileName(files[0].name)
                if (files) {
                setImage(URL.createObjectURL(files[0]))
                setErrorMessage('');
                }
            }}/>
            <div id="img-view">
                <img src="src/images/cloud-upload.png"/>
                <p>Click here to upload an image</p>
                <span>Supported format: .jpeg, .png, .jpg</span>
            </div>
            </label>
        </form> 
        <h2 className="inter-header-bold">Image Downloaded</h2>
        <section className="uploaded-row">
            < AiFillFileImage color='#1475cf'/>
            <span className="upload-content">            
            { fileName }
            <MdDelete onClick={() => {
                setFileName("No Selected File - ")
                setImage(null)
                form.reset();
            }}/>
            </span>
        </section>
        <div id="center-button">
            <button type="submit" form="upload-form" id="results" onClick={() => {
                setErrorMessage('')
            }
                }>See Results</button>
        </div>
        {errorMessage && <div className="response-message">{errorMessage}</div>}
        </>
    )
}

export default Uploader