#!/usr/bin/python3
"""Script that start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """definition hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """definition HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """defintion display text """
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """defintion diplay text"""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """defintion display number"""
    return "{:d} is a number".format(n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """defintion isplay a HTML page"""
    if n % 2 == 0:
        ev = 'even'
    else:
        ev = 'odd'
    return render_template('7-state_list.html', number=n, ev = ev)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ defintion list states """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    """ defintion close function """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
