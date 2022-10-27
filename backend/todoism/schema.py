import uuid

from marshmallow import Schema, fields, validate, pre_load, post_load 
from werkzeug.security import generate_password_hash

from todoism.db_models import User, List, Task


class UserSchema(Schema):
    """Schema for User JSON post/put data validation
    Returns a User model object post-validation.
    """
    id = fields.UUID(load_default=uuid.uuid4)
    username = fields.Str(
            required = True,
            validate = validate.Length(min=4)
    )
    password = fields.Str(
            required = True,
            validate = validate.Length(min=8)
    )

    @post_load
    def make_user(self, data, **kwargs):
        data['id'] = data['id'].bytes
        data['password'] = generate_password_hash(data['password'])
        return User(**data)


class TaskSchema(Schema):
    """Schema for Task JSON post/put data validation"""
    name = fields.Str(required=True)
    description = fields.Str()
    dueDate = fields.DateTime(required=True)
    listID = fields.Int(required=True)
    priority = fields.Str()
    id = fields.Int(dump_only=True)

    @post_load
    def make_task(self, data, **kwargs):
        return Task(**data)


class ListSchema(Schema):
    """Schema for List JSON post/put data validation"""
    name = fields.Str(
      required = True,
    )
    description = fields.Str()
    userID = fields.UUID(required=True, load_only=True)
    tasks = fields.List(fields.Nested(TaskSchema), dump_only=True)
    id = fields.Int(dump_only=True)

    @post_load
    def make_list(self, data, **kwargs):
        data['userID'] = data['userID'].bytes
        return List(**data)


