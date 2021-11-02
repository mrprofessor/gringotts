from flask import json, jsonify
from app.common.utils import status_codes


class APIException(Exception):
    status_code = status_codes.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, detail=None, status_code=None, payload=None):
        Exception.__init__(self)
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = detail
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        if self.detail:
            rv["error"] = {}
            rv["error"]["message"] = self.detail

        return rv

    def __str__(self):
        return self.detail


class ServiceException(APIException):
    def __init__(
        self,
        detail,
        status_code=status_codes.HTTP_422_UNPROCESSABLE_REQUEST,
        payload=None,
    ):
        super().__init__(detail, status_code, payload)


class AuthenticationException(APIException):
    status_code = status_codes.HTTP_401_UNAUTHORIZED
    detail = "Incorrect authentication credentials"


class NotFoundException(APIException):
    status_code = status_codes.HTTP_404_NOT_FOUND
    detail = "This resource does not exist"


class ValidationException(APIException):
    status_code = status_codes.HTTP_400_BAD_REQUEST
    detail = "One or more parameters to the API were invalid"


class SystemException(APIException):
    detail = "The system has encountered an internal error"
    status_code = status_codes.HTTP_500_INTERNAL_SERVER_ERROR
