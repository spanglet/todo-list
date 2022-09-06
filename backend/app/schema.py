from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    """Schema for User JSON post/put data validation"""
    username = fields.Str(required = True)
    password = fields.Str(required = True)

class ListSchema(Schema):
    """Schema for List JSON post/put data validation"""
    name = fields.Str(
      required = True,
      validate = validate.Length(min=2,max=16)
    )
    description = fields.Str()
    id = fields.Integer()

class TaskSchema(Schema):
    """Schema for Task JSON post/put data validation"""
    name = fields.Str(required=True)
    description = fields.Str()
    trueDueDate = fields.Date()
    listID = fields.Int()
    priority = fields.Str()
    id = fields.Int()
