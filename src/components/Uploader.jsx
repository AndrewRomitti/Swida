import React, { useState } from 'react'
import './Uploader.css'
import { MdCloudUpload, MdDelete} from 'react-icons/md'
import { AiFillFileImage } from 'react-icons/ai'

function Uploader() {
    const [image, setImage] = useState(null)
    const [fileName, setFileName] = useState("No Selected File - ")
    const [responseMessage, setResponseMessage] = useState('')

    const handleUploadImage = (ev) => {
        ev.preventDefault(); // Prevent the default form submission

        const fileInput = document.getElementById('input-file');
        const data = new FormData();
        data.append('file', fileInput.files[0]); // Append the selected file

        fetch('http://127.0.0.1:5001/upload', {
            method: 'POST',
            body: data,
        })
        .then((response) => response.text())
        .then((body) => {
            console.log('Upload successful:', body); // Log the response from the backend
            setResponseMessage(body);
        })
        .catch((error) => {
            console.error('Upload failed:', error);
            setResponseMessage('Upload failed. Please try again.');
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
            }}/>
            </span>
        </section>
        <div id="center-button">
            <button type="submit" form="upload-form" id="results">See Results</button>
        </div>
        {responseMessage && <div className="response-message">{responseMessage}</div>}
        </>
    )
}

export default Uploader