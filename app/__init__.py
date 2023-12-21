from flask import Flask

from app.api import test


def create_app():
    """Flask application factory"""

    app = Flask(__name__)

    test.init(app)

    return app


app = create_app()
