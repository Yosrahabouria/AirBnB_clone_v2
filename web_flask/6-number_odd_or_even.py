#!/usr/bin/python3
"""Script that start a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """definition hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """definition HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """defintion display text """
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """defintion diplay text"""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """defintion display number"""
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """defintion display a HTML page only """
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """defintion isplay a HTML page"""
    if n % 2 == 0:
        ev = 'even'
    else:
        ev = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
