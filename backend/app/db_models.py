from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.BINARY(16), primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trueDueDate = db.Column(
        db.DateTime,
        default = datetime.utcnow
    )
    priority = db.Column(
        db.Integer,
        default = 1
    )
    listID = db.Column(
        db.Integer,
        db.ForeignKey('list.id'),
        nullable = False
    )
    categoryID = db.Column(
        db.Integer,
        db.ForeignKey('category.id')
    )
    completed = db.Column(
        db.Boolean,
        default = False,
        nullable = False
    )

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    userID = db.Column(
        db.BINARY(16),
        db.ForeignKey('user.id')
    )

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    userID = db.Column(
        db.BINARY(16),
        db.ForeignKey('user.id')
    )

