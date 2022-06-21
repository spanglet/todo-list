from marshmallow import Schema, fields

class UserSchema(Schema):
    """Schema for User JSON post/put data validation"""
    username = fields.Str(required = True)
    password = fields.Str(required = True)

class ListSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()
    id = fields.Integer()

class TaskSchema(Schema):
    name=fields.Str(required=True)
    description=fields.Str()
    trueDueDate=fields.Date()
    listID=fields.Int()
    id = fields.Int()
