from flask import Blueprint, g
from werkzeug.exceptions import BadRequest
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import DBAPIError

from todoism.response import ErrorSchema, ErrorResponse
from todoism.exceptions import APIError

bp = Blueprint('error_handlers', __name__)

error_schema = ErrorSchema()

@bp.app_errorhandler(ValidationError)
def handle_validation_error(e):
    """Handles invalid JSON post/put request errors using marshmallow"""
    error = ErrorResponse(
        title = "JSON could not be validated",
        message = e.messages,
        status = 422
    )
    return error_schema.dump(error),422

@bp.app_errorhandler(403)
def handle_validation_error(e):
    error = ErrorResponse(
        title = "Access to resource is unauthorized",
        message = 'Unauthorized access to resource.',
        status = 403
    )
    return error_schema.dump(error), 403


@bp.app_errorhandler(BadRequest)
def handle_bad_request(e):
    """Handles invalid datatypes of request payloads"""
    error = ErrorResponse(
        title = "Invalid request datatype",
        message = e.description,
        status = 400
    )
    return error_schema.dump(error),400


@bp.app_errorhandler(401)
def handle_unauthorized_error(e):
    """Handle errors when login credentials are required for access"""
    error = ErrorResponse(
        title = "User is not authorized to access this resource",
        message = 'Login is required',
        status = 401
    )
    return error_schema.dump(error), 401


@bp.app_errorhandler(APIError)
def handle_login_error(e):
    """Handles custom exception raised when login fails"""
    return { 
        "error": {
            "title": e.title,
            "message": e.message,
            "status": e.status
        }
    }

    
