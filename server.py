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
    req_file = request.files['amf']
    if request.method == 'POST' and allowed_file_extensions(req_file.filename):
        filename = secure_filename(req_file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        req_file.save(upload_path)
        print(upload_path)
        return jsonify(message='File uploaded successfully' , path=upload_path)
    elif request.method =='POST' and 'amf' not in request.files : 
        return jsonify (message="You didn't attach amf dat file in the form")        
    return jsonify (message='You made a bad request, post request is required')