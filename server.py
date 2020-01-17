from flask import jsonify, Flask, request
app = Flask (__name__)


@app.route('/')
def home () :
    return jsonify(message="index route of the app")

@app.route('/amf', methods=['POST', 'GET'])
def index () :
    if request.method == 'POST':
        return jsonify(message='You hit the File upload route of the app')
    return jsonify (message='You made a bad request, post request is required')
    
