import mysql.connector
import json
from flask import Flask, render_template
from flask import request, Blueprint, jsonify
from .sql_util import connect_sql,insertRow, updateRow, removeRow, getAllRows
from marshmallow import Schema, fields, ValidationError

# Schema for JSON post/put data validation
class TaskSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()

app = Flask(__name__)

host = "mysqldb"
db = "flax"

bp = Blueprint('lists', __name__, url_prefix='/lists')


# Creates a new task list
@bp.route('/', methods=['POST','GET'])
def new_list():

  mydb = connect_sql(host, db)

  if request.method == 'POST':

    # Data must be of type json
    data = request.get_json()
    if not data:
        return "Data must be of type json",400
 
    # Use schema to check for incorrect request entries
    try:
        TaskSchema().load(data)

    except ValidationError:
        return "json contained incorrect keys",400
 
    # Insert response data into MySQL DB
    insertRow(mydb, "lists", data)
 
    return "list successfully added",200

  if request.method == 'GET':
    
    data = getAllRows(mydb,"lists")

    return data,200

# Delete or modify individual list        
@bp.route('/<list_id>', methods=['PUT','DELETE','GET'])
def update_list(list_id):

  data = request.get_json()
  mydb = connect_sql(host, db)

  # Update list with data of request if PUT request
  if request.method == 'PUT':
    updateRow(mydb, "lists", data)
    return "List was successfully updated",200

  # Remove list if DEL request received
  if request.method == 'DELETE':
    # todo: remove list from db
    removeRow(mydb, "lists", list_id)
    return "List was successfully removed",200
