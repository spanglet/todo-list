from flask import Blueprint
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError, DBAPIError

from .response import ErrorSchema, ErrorResponse

bp = Blueprint('error_handlers', __name__)

@bp.app_errorhandler(IntegrityError)
def handle_integrity_error(e):
    error = ErrorResponse(
        title = "Duplicate value error",
        message = str(e.orig.args[1]),
        status = 409
    )
    return ErrorSchema().dumps(error),409

@bp.app_errorhandler(ValidationError)
def handle_validation_error(e):
    """Handles invalid JSON post/put request errors using marshmallow"""
    error = ErrorResponse(
        title = "JSON could not be validated",
        message = e.messages,
        status = 422
    )
    return ErrorSchema().dumps(error),422

@bp.app_errorhandler(DBAPIError)
def handle_validation_error(e):
    """Undefined MySQL database error handler"""
    error = ErrorResponse(
        title = "Database action on server resulted in error.",
        message = e.messages,
        status = 500
    )
    return ErrorSchema().dumps(error),500
