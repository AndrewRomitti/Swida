import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import flask_cors
from flask_cors import CORS, cross_origin
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
# CORS(app, origins=["http://localhost:5173"], expose_headers='Authorization')
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
    response="success"
    return response

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host="0.0.0.0",port=5001, use_reloader=False)

flask_cors.CORS(app, expose_headers='Authorization')