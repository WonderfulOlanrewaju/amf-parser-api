from flask import jsonify, Flask, request
from werkzeug.utils import secure_filename
import os
import pandas as pd

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
    client_filename = file.filename
    if request.method == 'POST' and allowed_file_extensions(client_filename):
        filename = secure_filename(client_filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)
        # print(upload_path)
        converted = pd.read_fwf(upload_path)
        # print (type(converted))
        print (converted.iat[30,0])
        # print (dir(converted))
        os.remove(upload_path)
        return jsonify(message='Your file {} uploaded successfully'.format(client_filename))
    return jsonify (message='You made a bad request, post request is required')