from flask import Flask, request

app = Flask(__name__)


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
