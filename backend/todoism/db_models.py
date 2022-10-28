from datetime import date

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.BINARY(16), primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    dueDate = db.Column(
        db.Date,
        default = date.today()
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


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    userID = db.Column(
        db.BINARY(16),
        db.ForeignKey('user.id')
    )
    tasks = db.relationship('Task')

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    userID = db.Column(
        db.BINARY(16),
        db.ForeignKey('user.id')
    )
