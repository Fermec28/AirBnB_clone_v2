#!/usr/bin/python3
"""Module 0-hello_route"""

from flask import Flask, escape, render_template

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

if __name__ == '__main__':
            app.run(host='0.0.0.0', port=5000, debug=True)
