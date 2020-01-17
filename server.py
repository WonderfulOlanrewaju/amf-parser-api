from flask import jsonify, Flask, request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/amf'
ALLOWED_EXTENSIONS = {'dat' '999'}

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
    if request.method == 'POST' and 'amf' in request.files:
        f = request.files['amf']
        return jsonify(message='You hit the File upload route of the app')
    elif request.method =='POST' and 'amf' not in request.files : 
        return jsonify (message="You didn't attach amf dat file in the form")
    return jsonify (message='You made a bad request, post request is required')