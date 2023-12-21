from http import HTTPStatus

from flask import Blueprint, jsonify

test = Blueprint("Test", __name__)


@test.route("/test")
def heath_check():
    """Route for application health check"""
    return jsonify(status="OK"), HTTPStatus.OK


def init(app):
    """Register the Blueprint with an injected Flask application"""
    app.register_blueprint(test)
