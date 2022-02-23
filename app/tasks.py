import mysql.connector
import json
from flask import Flask, render_template
from flask import request, Blueprint, jsonify
from .sql_util import connect_sql
from .sql_util import insertRow
from marshmallow import Schema, fields, ValidationError

class TaskSchema(Schema):
    name=fields.Str()
    description=fields.Str()

app = Flask(__name__)

host = "mysqldb"
db = "flax"

bp = Blueprint('tasks', __name__, url_prefix='/tasks')


@bp.route('/list')
def get_tasks():
  mydb = connect_sql(host, db)
  cursor = mydb.cursor()

  cursor.execute("SELECT * FROM tasks")

  row_headers=[x[0] for x in cursor.description] #this will extract row headers

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))


  cursor.close()


  return jsonify(json_data)


# Creates a new task into the database
#
@bp.route('/new_task', methods=['POST'])
def new_task():

  # New task information is in request
  # Data must be of type json
  data = request.get_json()
  if not data:
      return "Data must be of type json",400


  mydb = connect_sql(host, db)

  # Insert response data into MySQL DB

  #Use schema to check for incorrect request entries
  try:

      TaskSchema().load(data)

  except ValidationError:

      return "json contained incorrect keys",400


  insertRow(mydb, "tasks", [data["name"], data["description"]])

  return 'task successfully created',200


@bp.route('/initdb')
def db_init():
  mydb = connect_sql(host, None)
  cursor = mydb.cursor()

  print("Creating Database")
  cursor.execute("DROP DATABASE IF EXISTS flax")
  cursor.execute("CREATE DATABASE flax")
  cursor.close()

  taskTable = '''
    name VARCHAR(255), 
    taskID INTEGER NOT NULL AUTO_INCREMENT,
    description VARCHAR(255),
    categoryID INTEGER,
    priority INTEGER,
    trueDueDate DATETIME,
    preferredDueDate DATETIME,
    dependantsID INTEGER REFERENCES Tasks(taskID),
    startDate DATETIME,
    primary Key (taskID),
    foreign Key (categoryID) REFERENCES categories(categoryID)
  '''

  categoryTable = '''
    name VARCHAR(255), 
    categoryID INTEGER NOT NULL,
    description VARCHAR(255),
    primary Key (categoryID)
  '''
  mydb = connect_sql(host, db)
  cursor = mydb.cursor()

  # Drop Tables if previously created
  cursor.execute("DROP TABLE IF EXISTS tasks")
  cursor.execute("DROP TABLE IF EXISTS categories")

  cursor.execute("CREATE TABLE categories ({})".format(categoryTable))
  cursor.execute("CREATE TABLE tasks ({})".format(taskTable))
  cursor.close()

  return 'init database'

if __name__ == "__main__":
  app.run(debug=True,host ='0.0.0.0')
