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
        nullable = False,
        default = datetime.utcnow
    )
    listID = db.Column(
        db.Integer,
        db.ForeignKey('list.id'),
        nullable=False
    )
    categoryID = db.Column(
        db.Integer,
        db.ForeignKey('category.id')
    )

    #dependantsID INTEGER REFERENCES Tasks(id),
    #priority INTEGER,
    #preferredDueDate DATETIME,

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
