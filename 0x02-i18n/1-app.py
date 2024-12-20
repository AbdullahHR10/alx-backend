#!/usr/bin/env python3
""" Module that contains a basic Flask app with Babel. """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ Configures available languages in Flask app. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def hello_world():
    """ Returns '1-index.html' """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
