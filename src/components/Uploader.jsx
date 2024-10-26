import React, { useState } from 'react'
import './Uploader.css'
import { MdCloudUpload, MdDelete} from 'react-icons/md'
import { AiFillFileImage } from 'react-icons/ai'

function Uploader() {
    const [image, setImage] = useState(null)
    const [fileName, setFileName] = useState("No Selected File - ")
    return (
        <>
        <form>
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
        </>
    )
}

export default Uploader