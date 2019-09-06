#!/usr/bin/python3
"""Module 0-hello_route"""

from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbtn():
        """ hello world with flask"""
        return 'Hello HBNB!'


@app.route('/hbnb')
def hbtn():
        """ hello world with flask"""
        return 'HBNB'


@app.route('/c/<text>')
def c_request(text):
        """ route pattern """
        return 'C %s' % escape(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_request(text='is cool'):
        """ route pattern """
        return 'Python %s' % escape(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_request(n):
        """ number """
        return '%d is a number' % n


@app.route('/number_template/<int:number>')
def number_template(number):
        """ number in template """
        return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:number>')
def number_odd_even(number):
        """ number in template """
        return render_template('6-number_odd_or_even.html', number=number)


@app.route('/states_list')
def states():
        """ number in template """
        states = list(storage.all("State").values()).copy()
        states.sort(key=lambda x: x.name)
        return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def states_cities():
        """ number in template """
        states = list(storage.all("State").values()).copy()
        states.sort(key=lambda x: x.name)
        return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<id>')
def states_show(id):
        """ number in template """
        state = State.find(id)
        return render_template('9-states.html', state=state, states=None)


@app.route('/states')
def index_state():
        """ number in template """
        states = list(storage.all("State").values()).copy()
        print(states)
        states.sort(key=lambda x: x.name)
        return render_template('9-states.html', state=None, states=states)


@app.route('/hbnb_filters')
def airbnb():
        """ number in template """
        states = list(storage.all("State").values()).copy()
        states.sort(key=lambda x: x.name)
        amenities = list(storage.all("Amenity").values()).copy()
        amenities.sort(key=lambda x: x.name)
        return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_conection(exeption=None):
        storage.close()

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)
