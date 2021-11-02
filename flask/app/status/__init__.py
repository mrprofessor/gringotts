from flask import Blueprint
from app.status.views import status_view

# Define blueprint that will be registered by main app
status_api = Blueprint("status_api", __name__)
status_view.StatusView.register(status_api)
