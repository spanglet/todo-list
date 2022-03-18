import mysql.connector
import json
from flask import Flask, render_template
from flask import request, Blueprint, jsonify
from .sql_util import insertRow, updateRow, removeRow, connect_sql
from marshmallow import Schema, fields, ValidationError

# Schema for JSON post/put data validation
class TaskSchema(Schema):
    name=fields.Str(required=True)
    description=fields.Str()
    trueDueDate=fields.Date()
    listID=fields.Int()

app = Flask(__name__)

host = "mysqldb"
db = "flax"

bp = Blueprint('tasks', __name__, url_prefix='/tasks')


# Creates a new task into the database
#
@bp.route('/', methods=['POST','GET'])
def manage_tasks():

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
    task_id = insertRow(mydb, "tasks", data)
 
    return "task successfully added",200

  # GET requests for entire contents of tasks in db
  if request.method == 'GET':

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM tasks")
 
    row_headers=[x[0] for x in cursor.description] 
 
    results = cursor.fetchall()
    json_data=[]
    for result in results:
      json_data.append(dict(zip(row_headers,result)))
 
    cursor.close()
 
    return jsonify(json_data)


@bp.route('/<task_id>', methods=['PUT','DELETE','GET'])
def update_task(task_id):

  data = request.get_json()
  mydb = connect_sql(host, db)

  # Update task with data of request if PUT request
  if request.method == 'PUT':
    updateRow(mydb, "tasks", data)
    return "Task was successfully updated",200

  # Remove task if DEL request received
  if request.method == 'DELETE':
    # todo: remove task from db
    removeRow(mydb, "tasks", task_id)
    return "Task was successfully removed",200
    
