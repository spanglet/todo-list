import json
from flask import Flask, render_template
from flask import request, Blueprint, jsonify
from marshmallow import Schema, fields, ValidationError

from .db_models import db,Task
from .auth import login_required
from .schema import TaskSchema

# Schema for JSON post/put data validation

bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@login_required
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
                listID = data["listID"]
            )
            db.session.add(new_task)
            db.session.commit()
 
        except ValidationError:
            return "json contained incorrect keys",400
  
        return "task successfully added",200

    # GET requests for entire contents of tasks in db
    if request.method == 'GET':

        try:
            tasks = Task.query.filter(List.userID == session["user_id"]).all() 
        except:
            return "Error in querying all records from Task table", 404

        json_tasks = TaskSchema(many=True).dumps(tasks)
 
        return json_tasks, 200


@bp.route('/<task_id>', methods=['PUT','DELETE','GET'])
def update_task(task_id):

  # Update task with data of request if PUT request
    if request.method == 'PUT':
        
        data = request.get_json()

        task = Task.query.get(task_id)
       
        # Update Task object that was retrieved
        for key,val in data.items():
            setattr(task,key,val)

        db.session.commit()
        return "Task was successfully updated",200

    # Remove task if DEL request received
    if request.method == 'DELETE':

        del_task = Task.query.get(task_id)
        db.session.delete(del_task)
        db.session.commit()
        return "Task was successfully removed",200
