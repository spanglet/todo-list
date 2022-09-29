"""Standard response JSON body"""
from marshmallow import Schema, fields, validate, validates_schema, post_dump

class ErrorResponse:
    """Standard response structure for errors in API"""
    def __init__(self,status,message,title):
        self.status = status
        self.message = message
        self.title = title

class DataResponse:
    """Successful API response structure."""
    def __init__(self,content):
        self.content = content

class ErrorSchema(Schema):
    """Standard error response schema for API"""
    status = fields.Int(required=True)
    message = fields.Str(required=True)
    title = fields.Str()

    @post_dump
    def wrap_error(self, data, **kwargs):
        return {"error": data}
    
class DataSchema(Schema):
    """Standard schema for successful API response"""
    content = fields.List(fields.Dict(),required = True)

    @post_dump
    def wrap_data(self, data, **kwargs):
        return {"data": data}
