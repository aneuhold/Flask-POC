from flask import Flask
from flask import request


def create_app(config_filename=None):
    """
    Creates the application. This is useful for testing.
    """
    app = Flask(__name__)

    if config_filename is not None:
        app.config.from_pyfile(config_filename)

    return app


app = create_app()


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
