import os
from flask import Flask, flash, request, redirect, url_for, session, jsonify
from werkzeug.utils import secure_filename
import flask_cors
from flask_cors import CORS, cross_origin
import logging
import hf_pred as lung
import gradcam
import treatment
import explanation
import base64
import io
import educationalResources
import gradcamAnalysis
import testMime

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
CORS(app, expose_headers='Authorization')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def fileUpload():
    target=os.path.join(UPLOAD_FOLDER,'images')
    if not os.path.isdir(target):
        os.mkdir(target)
        
    logger.info("welcome to upload`")
    
    file = request.files['file'] 
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath'] = destination
    
    lungModelPrediction = lung.predict(destination)
    print(f"The result is: {lungModelPrediction} ({type(lungModelPrediction)})")
    
    gradcam_img = gradcam.compute_gradcam(destination)
    buffer = io.BytesIO()
    gradcam_img.save(buffer, format="PNG")
    gradcam_image_bytes = buffer.getvalue()
    encoded_string = base64.b64encode(gradcam_image_bytes).decode("utf-8")

    # LLM Prompting
    explanationText = explanation.generate_content(lungModelPrediction)
    treatmentText = treatment.generate_content(lungModelPrediction)
    resourcesArr = educationalResources.getEducationalResources(lungModelPrediction)
    analysisText = gradcamAnalysis.generate_content(gradcam_image_bytes, lungModelPrediction)
    
    mime_type = testMime.get_mime_type_from_bytes(gradcam_image_bytes)
    print(mime_type)

    
    response = {
        "diagnosis": lungModelPrediction,
        "gradcam": encoded_string,
        "explanation": explanationText,
        "treatment": treatmentText,
        "resources": resourcesArr,
        "analysis": analysisText
    }

    return jsonify(response)

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host="0.0.0.0",port=5001, use_reloader=False)

flask_cors.CORS(app, expose_headers='Authorization')