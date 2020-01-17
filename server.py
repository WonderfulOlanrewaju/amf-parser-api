from flask import jsonify, Flask, request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'amf'
ALLOWED_EXTENSIONS = {'dat','999'}

app = Flask (__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# utility function for checking uploaded files conform to allowed extensions format
def allowed_file_extensions (filename) : 
    return '.' in filename and \
        filename.rsplit('.', 1) [1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home () :
    return jsonify(message="index route of the app")

@app.route('/amf', methods=['POST', 'GET'])
def index () :
    file = request.files['amf']
    if request.method == 'POST' and allowed_file_extensions(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify(message='You hit the File upload route of the app')
    return jsonify (message='You made a bad request, post request is required')