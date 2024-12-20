#!/usr/bin/env python3
""" Module that contains a basic Flask app. """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """ Returns '0-index.html' """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
