from flask import Blueprint
from app.passwords.views import passwords_view
from .password_management import PasswordManagement

# Define blueprint that will be registered by main app
passwords_api = Blueprint("passwords_api", __name__)
passwords_view.PasswordsView.register(passwords_api)
