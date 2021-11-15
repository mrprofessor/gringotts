from flask import Flask, request
from flask_cors import CORS
import os


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

def load_config(app):
    """ Load config for config.py """
    from .configurations import APP_CONFIG, ProductionConfig

    # TODO
    # Figure out, why it's failing while using docker-compose
    # environment_configuration = os.environ['CONFIG_ENV']
    # app.config.from_object(APP_CONFIG.get(environment_configuration)())
    app.config.from_object(ProductionConfig())

def create_app(**kwargs):
    app = Flask(__name__, **kwargs)
    load_config(app)
    register_error_handlers(app)
    CORS(app)

    with app.app_context():
        register_blueprints(app)

    return app
