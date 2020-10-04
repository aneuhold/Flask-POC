# Development

To build the environment for the first time you can use

```
. venv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
rm get-pip.py
pip install Flask
export FLASK_APP=server.py
pip install Flask-CORS
pip install pytest
```

To startup the development environment, use the following commands:

```
. venv/bin/activate
export FLASK_APP=server.py
```

To start the flask server use

```
flask run
```

To exit the Python development environment use

```
deactivate
```