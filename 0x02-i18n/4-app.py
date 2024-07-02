#!/usr/bin/env python3
'''
    Flask app with Babel and locale selection
'''

from flask_babel import Babel
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    '''
        Configuration for Flask app with Babel.
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def helloWorld() -> str:
    '''
        Render the home page with a welcome message.
    '''
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    '''
        Determine the best match for supported languages.
    '''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
