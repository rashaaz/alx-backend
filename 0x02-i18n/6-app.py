#!/usr/bin/env python3
'''
    Flask app with Babel, user mock login
'''

from flask_babel import Babel
from flask import Flask, render_template, request, g
from typing import Union

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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    '''
        Get user from the mock database
    '''
    try:
        login_as = request.args.get('login_as', None)
        user = users[int(login_as)]
    except Exception:
        user = None


@app.before_request
def before_request():
    '''
        Set user in global g before each request.
    '''
    user = get_user()
    g.user = user


@app.route('/', methods=['GET'], strict_slashes=False)
def helloWorld() -> str:
    '''
        Render the home page with a welcome message.
    '''
    return render_template('6-index.html')


@babel.localeselector
def get_locale() -> str:
    '''
        Determine the best match for supported languages
    '''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
