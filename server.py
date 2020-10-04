from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'You used a POST request'
    else:
        return 'you did not use a POST request'
