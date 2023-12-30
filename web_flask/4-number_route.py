#!/usr/bin/python3
""" script to start a flask web application """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/', strict_slashes = False)
def hello():
    """ returns text """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_2():
    """returns hbnb"""
    return 'hbnb'


@app.route('/c/<text>')
def c_text(text):
    """ replace text with variable. """
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ replace more text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    """ replace with int only if given int. """
    n = str(n)
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

