import os

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

from social_flask.routes import social_auth
from social_flask_sqlalchemy.models import init_social

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://backend:backend@localhost/backend'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SOCIAL_AUTH_USER_MODEL'] = 'models.User'
app.config['SOCIAL_AUTH_AUTHENTICATION_BACKENDS'] = (
    'social_core.backends.google.GoogleOAuth2',
)
app.config['SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'] = os.environ['GOOGLE_CLIENT_ID']
app.config['SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'] = os.environ['GOOGLE_CLIENT_SECRET']
app.config['SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA'] = [('Pie', 'Face')]

app.register_blueprint(social_auth)
db = SQLAlchemy(app)

init_social(app, session)

@app.before_request
def global_user():
    g.user = get_current_logged_in_user


@app.route('/')
def hello_world():
    return '<a href="/login/google-oauth2/">Hello, World!</a>'
