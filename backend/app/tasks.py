import json
from flask import Flask, render_template
from flask import request, Blueprint, jsonify
from marshmallow import Schema, fields, ValidationError

from .db_models import db,Task

# Schema for JSON post/put data validation
class TaskSchema(Schema):
    name=fields.Str(required=True)
    description=fields.Str()
    trueDueDate=fields.Date()
    listID=fields.Int()

bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@bp.route('/', methods=['POST','GET'])
def manage_tasks():

    if request.method == 'POST':

        # Data must be of type json
        data = request.get_json()
        if not data:
            return "Data must be of type json",400
  
        # Use schema to check for incorrect request entries
        try:
            TaskSchema().load(data)
            new_task = Task(
                name = data["name"],
                description = data["description"],
                trueDueDate = data["trueDueDate"],
                listID = fields.Int()
            )
            db.session.add(new_task)
            db.session.commit()
 
        except ValidationError:
            return "json contained incorrect keys",400
  
        return "task successfully added",200

  # GET requests for entire contents of tasks in db
    if request.method == 'GET':

        try:
            tasks = Task.query.all() 
        except:
            return "Error in querying all records from Task table", 404
 
        return jsonify(tasks),200


@bp.route('/<task_id>', methods=['PUT','DELETE','GET'])
def update_task(task_id):

  # Update task with data of request if PUT request
    if request.method == 'PUT':
        
        data = request.get_json()
        task = Task.get(task_id)
       
        # Update Task object that was retrieved
        for key,val in data.items():
            setattr(task,key,val)

        db.session.commit()
        return "Task was successfully updated",200

    # Remove task if DEL request received
    if request.method == 'DELETE':

        db.session.delete(task_id)
        db.session.commit()
        return "Task was successfully removed",200
