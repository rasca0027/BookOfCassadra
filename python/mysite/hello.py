from flask import Flask, request
app = Flask(__name__)

@app.route('/predict', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        print request.form
        return '200 OK'
    return 'Hello world'
