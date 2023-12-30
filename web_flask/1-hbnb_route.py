#!/usr/bin/env python3

""" script to start a simple web app with 2 routes """

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """ returns Hello HBNB. """
    return 'Hello HBNB!'



@app.route('/hbnb', strict_slashes=False)
def hello_2():
    """ returns HBNB. """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
