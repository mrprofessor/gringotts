from flask import request, make_response, jsonify
from flask import current_app as app
from flask_classful import FlaskView
from marshmallow import ValidationError

from app.common.representations.default import output_json
from app.common.exceptions import ValidationException


class BaseView(FlaskView):
    representations = {"application/json": output_json}

    authorization_exempt = []
    authentication_exempt = []

    def parse_url_params(self):
        r_params = {
            "and": {
                k.replace("_and_", ""): v
                for k, v in request.args.items()
                if k.startswith("_and_")
            },
            "in": {
                k.replace("_in_", ""): [i for i in v.split(",") if i]
                for k, v in request.args.items()
                if k.startswith("_in_")
            },
        }
        return r_params

    def load_input_data(self, schema, data):
        """ Load and validate input data """
        try:
            result = schema.load(data)
            return result
        except ValidationError as err:
            # FIXME
            # err.messages will break if exception arises due to a different
            # exception
            # result = jsonify({"message": FAILURE_MSG, "error_fields": err.messages})
            # return result, 400
            raise ValidationException(payload=err.messages)
