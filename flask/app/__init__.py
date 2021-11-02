from flask import Flask, request
from flask_cors import CORS


def register_blueprints(app):
    """ Register all API blueprints here """
    from app.status import status_api
    from app.passwords import passwords_api

    app.register_blueprint(status_api, url_prefix="/api/")
    app.register_blueprint(passwords_api, url_prefix="/api/")

def register_error_handlers(app):
    """Registers global error handlers for exception types.
    These can be overridden in the views if needed"""
    from app.common.exceptions import APIException, handle_validation_error

    app.register_error_handler(APIException, handle_validation_error)

def create_app(**kwargs):
    app = Flask(__name__, **kwargs)
    register_blueprints(app)
    register_error_handlers(app)
    CORS(app)
    return app
