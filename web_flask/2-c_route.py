#!/usr/bin/python3
"""Module 0-hello_route"""

from flask import Flask, escape

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
if __name__ == '__main__':
            app.run(host='0.0.0.0', port=5000, debug=True)
