from datetime import datetime

from __init__ import app


host = "mysqldb"
db = "flax"

def init_db():

    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb:root@127.0.0.1:3306/mysqldb"


    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255)),
    description = db.Column(db.String(255)),
    trueDueDate = db.Column(db.DateTime,
            nullable=false,
            default=datetime.utcnow),
    listID = db.Column(db.Integer,
            db.ForeignKey('list.id'),
            nullable=False),
    categoryID = db.Column(db.String, db.ForeignKey('category.id'))
    #dependantsID INTEGER REFERENCES Tasks(id),
    #priority INTEGER,
    #preferredDueDate DATETIME,

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True),
    name = db.Column(db.String(255)),
    description VARCHAR(255),

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255)),
    description = db.Column(db.String(255)),

class User
    id = db.Column(db.Integer, primary_key=True),
    username = db.Column(db.String(255), unique=True),

    password VARCHAR(255) NOT NULL
  '''

