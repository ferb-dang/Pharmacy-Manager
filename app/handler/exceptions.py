# -*- coding: utf-8 -*-
import logging

from fastapi.exceptions import RequestValidationError
from jwt.exceptions import PyJWTError
from slowapi.errors import RateLimitExceeded
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse
from starlette_i18n import gettext_lazy as _

from handler.error_code import *

logger = logging.getLogger(__file__)


def http_status_message(status_code):
    return HTTP_STATUS_CODES.get(status_code, '')



def error_data(error_code, message, params=""):
    if params:
        params = ','.join(params)
    else:
        params = ''
    error = {
        'status': error_code,
        'detail': str(message),
        'params': params
    }
    return error


class APIException(Exception):
    status_code = 500
    http_status_code = HTTP_500_INTERNAL_SERVER_ERROR
    params = []

    def __init__(self, error_code=None, *args, params: list = []):
        if error_code in self.http_status_code:
            self.error_code = error_code
        else:
            self.error_code = self.status_code
        message = self.http_status_code.get(error_code, http_status_message(self.status_code))
        self.message = message.format(*args)
        self.params = params

    @property
    def description(self):
        return error_data(self.error_code, self.message, self.params)


class BadRequest(APIException):
    status_code = 400
    http_status_code = HTTP_400_BAD_REQUEST


class Unauthorized(APIException):
    status_code = 401
    http_status_code = HTTP_401_UNAUTHORIZED


class Forbidden(APIException):
    status_code = 403
    http_status_code = HTTP_403_FORBIDDEN


class NotFound(APIException):
    status_code = 404
    http_status_code = HTTP_404_NOT_FOUND


class MethodNotAllowed(APIException):
    status_code = 405
    http_status_code = HTTP_405_METHOD_NOT_ALLOWED


class NotAcceptable(APIException):
    status_code = 406
    http_status_code = HTTP_406_NOT_ACCEPTABLE


class Conflict(APIException):
    status_code = 409
    http_status_code = HTTP_409_CONFLICT


class OverLimit(APIException):
    status_code = 413
    http_status_code = HTTP_413_REQUEST_ENTITY_TOO_LARGE


class UnsupportedMediaType(APIException):
    status_code = 415
    http_status_code = HTTP_415_UNSUPPORTED_MEDIA_TYPE


class UnprocessableEntity(APIException):
    status_code = 422
    http_status_code = HTTP_422_UNPROCESSABLE_ENTITY


class RateLimit(APIException):
    status_code = 429
    http_status_code = HTTP_429_TOO_MANY_REQUESTS


class InternalServerError(APIException):
    status_code = 500
    http_status_code = HTTP_500_INTERNAL_SERVER_ERROR
