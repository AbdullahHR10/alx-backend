#!/usr/bin/env python3
""" Module that contains a basic Flask app with Babel
and dynamic locale selection. """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ Configures available languages in Flask app. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Determines the best match for supported languages.
    Checks for locale in request args and defaults to best match."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
    """ Returns '1-index.html' """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)