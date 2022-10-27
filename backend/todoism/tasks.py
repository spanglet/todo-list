import json
from flask import (
    Flask, render_template, request,
    Blueprint, jsonify, session, g
)

from todoism.db_models import db, Task, List
from todoism.auth import login_required
from todoism.schema import TaskSchema

# Schema for JSON post/put data validation

bp = Blueprint('tasks', __name__, url_prefix='/tasks')


@bp.route('/', methods=['POST','GET'])
@login_required
def manage_tasks():

    if request.method == 'POST':

        # Data must be of type json
        data = request.get_json()
  
        # Use schema to check for incorrect request entries
        new_task = TaskSchema().load(data)

        db.session.add(new_task)
        db.session.commit()
  
        return {"ok": True}, 201

    else:
        # GET requests for entire contents of tasks in db
        query = db.select(Task).join(List.tasks).where(List.userID == g.user.id)

        tasks = db.session.execute(query).scalars().all()

        data = TaskSchema(many=True).dump(tasks)
 
        return jsonify(data), 200


@bp.route('/<int:task_id>', methods=['PUT','DELETE','GET'])
@login_required
def update_task(task_id):

    task = db.get_or_404(Task, task_id)

    if request.method == 'PUT':
        
        data = request.get_json()

        #TODO Task validation

        # Update Task object by data key-value pairs
        for key,val in data.items():
            setattr(task, key, val)

        db.session.commit()

        return { 
            "ok": True,
            "message": "Task was successfully updated",
        }, 200

    elif request.method == 'DELETE':

        db.session.delete(task)
        db.session.commit()

        return { 
            "ok": True,
            "message": "Task was successfully removed",
            "id": task_id,
        }, 200

    else:
        return TaskSchema().dump(task), 200
