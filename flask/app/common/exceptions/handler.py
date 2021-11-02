from flask import jsonify
from app.common.representations import output_json


def handle_validation_error(error):
    return output_json(error.to_dict(), error.status_code)
