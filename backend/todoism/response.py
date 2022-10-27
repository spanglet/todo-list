"""Standard response JSON body"""
from marshmallow import Schema, fields, validate, validates_schema, post_dump

class ErrorResponse:
    def __init__(self, message, status=200, title="An error occured"):
        self.message = message
        self.status = status
        self.title = title

class ErrorSchema(Schema):
    """Standard error response schema for API"""
    message = fields.Str(required=True)
    status = fields.Int(dump_default=200)
    title = fields.Str()

    @post_dump
    def wrap_error(self, data, **kwargs):
        return {"error": data}
    
