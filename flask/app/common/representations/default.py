from flask import make_response, jsonify

SUCCESS_STATUS = "success"
ERROR_STATUS = "error"


def output_json(output, status_code, headers=None):
    """
    Generates JSON response object for view functions
    See Flask-Classful docs for usage on views:
        http://flask-classful.teracy.org/index.html?highlight=representation
    :param output: list or dict returned from view function
    :param status_code: http status code
    :param headers: dict to use for reponse header
    :return: response
    """
    content_type = "application/json"

    # Check whether the output is a dictionary or list
    if isinstance(output, dict):
        # If output already has data key we assume the
        # output should be returned as is.
        if output.get("data") is None:
            payload = {"data": output}
        else:
            payload = output
    elif isinstance(output, list):
        payload = {"data": output}
    else:
        raise TypeError(
            f"type {type(output)} is not currently" f" supported for json output"
        )

    status = SUCCESS_STATUS if status_code < 400 else ERROR_STATUS
    payload["status"] = status

    if headers:
        headers.update({"Content-Type": content_type})
    else:
        headers = {"Content-Type": content_type}
    response = make_response(jsonify(payload), status_code, headers)
    return response
