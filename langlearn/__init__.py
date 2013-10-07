from flask import Flask
from langlearn.database import db_session
import logging
import os

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


@app.teardown_request
def shutdown_session(exception=None):
    """
    Shutdown the database session.
    """
    db_session.remove()


@app.before_first_request
def setup_logging():
    """
    Setup logging for the app.
    """
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.DEBUG)


import langlearn.routes
langlearn.routes
